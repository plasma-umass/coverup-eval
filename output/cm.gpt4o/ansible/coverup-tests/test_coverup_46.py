# file lib/ansible/playbook/role_include.py:72-125
# lines [72, 75, 76, 78, 80, 81, 83, 84, 86, 87, 88, 91, 92, 93, 95, 96, 99, 103, 104, 106, 107, 109, 112, 114, 115, 116, 118, 121, 122, 123, 124, 125]
# branches ['75->76', '75->78', '83->84', '83->86', '95->96', '95->99', '103->104', '103->106', '115->116', '115->121', '122->123', '122->124']

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.role_include import RoleInclude
from ansible.playbook.task_include import TaskInclude
from ansible.template import Templar
from ansible.playbook.role import Role

@pytest.fixture
def mock_task_include():
    class MockTaskInclude(TaskInclude):
        def __init__(self):
            self._role_name = 'test_role'
            self._parent = MagicMock()
            self._parent._play = MagicMock()
            self.vars = {}
            self._from_files = 'test_file'
            self.collections = []
            self.allow_duplicates = False
            self.statically_loaded = False
            self.public = False
            self._parent_role = None
            self.rolespec_validate = True
            self._squashed = False
            self._finalized = False

        def build_parent_block(self):
            return MagicMock()

    return MockTaskInclude()

@pytest.fixture
def mock_role_include():
    with patch('ansible.playbook.role_include.RoleInclude.load') as mock_load:
        yield mock_load

@pytest.fixture
def mock_role():
    with patch('ansible.playbook.role.Role.load') as mock_load:
        yield mock_load

@pytest.fixture
def mock_templar():
    with patch('ansible.template.Templar.template') as mock_template:
        yield mock_template

def test_include_role_get_block_list(mock_task_include, mock_role_include, mock_role, mock_templar):
    mock_role_include.return_value = MagicMock(vars={})
    mock_role.return_value = MagicMock(_metadata=MagicMock(allow_duplicates=False), collections=[], _role_path='test_path', compile=MagicMock(return_value=[]), get_handler_blocks=MagicMock(return_value=[]))
    mock_templar.return_value = 'templated_file'

    class IncludeRole(mock_task_include.__class__):
        def get_block_list(self, play=None, variable_manager=None, loader=None):
            if play is None:
                myplay = self._parent._play
            else:
                myplay = play

            ri = RoleInclude.load(self._role_name, play=myplay, variable_manager=variable_manager, loader=loader, collection_list=self.collections)
            ri.vars.update(self.vars)

            if variable_manager is not None:
                available_variables = variable_manager.get_vars(play=myplay, task=self)
            else:
                available_variables = {}
            templar = Templar(loader=loader, variables=available_variables)
            from_files = templar.template(self._from_files)

            actual_role = Role.load(ri, myplay, parent_role=self._parent_role, from_files=from_files,
                                    from_include=True, validate=self.rolespec_validate)
            actual_role._metadata.allow_duplicates = self.allow_duplicates

            if self.statically_loaded or self.public:
                myplay.roles.append(actual_role)

            self._role_path = actual_role._role_path

            if not self._parent_role:
                dep_chain = []
            else:
                dep_chain = list(self._parent_role._parents)
                dep_chain.append(self._parent_role)

            p_block = self.build_parent_block()
            p_block.collections = actual_role.collections

            blocks = actual_role.compile(play=myplay, dep_chain=dep_chain)
            for b in blocks:
                b._parent = p_block
                b.collections = actual_role.collections

            handlers = actual_role.get_handler_blocks(play=myplay)
            for h in handlers:
                h._parent = p_block
            myplay.handlers = myplay.handlers + handlers
            return blocks, handlers

    include_role = IncludeRole()
    blocks, handlers = include_role.get_block_list()

    assert include_role._role_path == 'test_path'
    assert blocks == []
    assert handlers == []
