# file lib/ansible/playbook/role_include.py:72-125
# lines [75, 76, 78, 80, 81, 83, 84, 86, 87, 88, 91, 92, 93, 95, 96, 99, 103, 104, 106, 107, 109, 112, 114, 115, 116, 118, 121, 122, 123, 124, 125]
# branches ['75->76', '75->78', '83->84', '83->86', '95->96', '95->99', '103->104', '103->106', '115->116', '115->121', '122->123', '122->124']

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.role import Role
from ansible.template import Templar

# Mock classes to avoid side effects and dependencies
class MockParent:
    _play = Play()

class MockRoleInclude(Role):
    @staticmethod
    def load(*args, **kwargs):
        return MockRoleInclude()

class MockRole(Role):
    @staticmethod
    def load(*args, **kwargs):
        mock_role = MockRole()
        mock_role._role_path = '/fake/path'
        mock_role._metadata = type('MockMetadata', (object,), {'allow_duplicates': False})
        mock_role.collections = []
        return mock_role

    def compile(self, *args, **kwargs):
        return []

    def get_handler_blocks(self, *args, **kwargs):
        return []

# Replace the Role and RoleInclude classes with mocks
@pytest.fixture(autouse=True)
def mock_classes(mocker):
    mocker.patch('ansible.playbook.role_include.RoleInclude', MockRoleInclude)
    mocker.patch('ansible.playbook.role_include.Role', MockRole)

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock(spec=VariableManager)

@pytest.fixture
def mock_play(mocker):
    play = mocker.MagicMock(spec=Play)
    play.handlers = []
    return play

def test_include_role_get_block_list(mock_loader, mock_variable_manager, mock_play):
    # Setup the IncludeRole instance with a mock parent
    include_role = IncludeRole()
    include_role._parent = MockParent()
    include_role._parent_role = None
    include_role._role_name = 'fake_role'
    include_role.vars = {}
    include_role._from_files = False
    include_role.statically_loaded = False
    include_role.public = False
    include_role.rolespec_validate = False
    include_role.allow_duplicates = False

    # Call the method under test
    blocks, handlers = include_role.get_block_list(play=mock_play, variable_manager=mock_variable_manager, loader=mock_loader)

    # Assertions to verify postconditions
    assert isinstance(blocks, list)
    assert isinstance(handlers, list)
    assert include_role._role_path == '/fake/path'
    assert mock_play.handlers == handlers  # This should not raise an AssertionError now

    # Cleanup is handled by the fixture scope and mocking
