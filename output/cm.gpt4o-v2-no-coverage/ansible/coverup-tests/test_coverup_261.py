# file: lib/ansible/playbook/role/include.py:36-60
# asked: {"lines": [36, 38, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}
# gained: {"lines": [36, 38, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.playbook.attribute import FieldAttribute
from ansible.playbook.role.definition import RoleDefinition
from ansible.module_utils._text import to_native
from ansible.playbook.role.include import RoleInclude

class MockLoader:
    def __init__(self, basedir="/mock_basedir"):
        self._basedir = basedir

    def get_basedir(self):
        return self._basedir

    def path_exists(self, path):
        return True

class MockVariableManager:
    def get_vars(self, play):
        return {}

@pytest.fixture
def mock_loader():
    return MockLoader()

@pytest.fixture
def mock_variable_manager():
    return MockVariableManager()

def test_role_include_init():
    play = object()
    role_basedir = "/path/to/role"
    variable_manager = object()
    loader = object()
    collection_list = []

    role_include = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    assert role_include._play == play
    assert role_include._role_basedir == role_basedir
    assert role_include._variable_manager == variable_manager
    assert role_include._loader == loader
    assert role_include._collection_list == collection_list

def test_role_include_load_invalid_data():
    with pytest.raises(AnsibleParserError, match="Invalid role definition: 123"):
        RoleInclude.load(123, play=object())

def test_role_include_load_invalid_old_style_role():
    with pytest.raises(AnsibleError, match="Invalid old style role requirement: old,style,role"):
        RoleInclude.load("old,style,role", play=object())

def test_role_include_load_valid_string_data(mock_loader, mock_variable_manager):
    play = object()
    data = "valid_role"
    role_include = RoleInclude.load(data, play=play, loader=mock_loader, variable_manager=mock_variable_manager)
    assert isinstance(role_include, RoleInclude)

def test_role_include_load_valid_dict_data(mock_loader, mock_variable_manager):
    play = object()
    data = {"role": "valid_role"}
    role_include = RoleInclude.load(data, play=play, loader=mock_loader, variable_manager=mock_variable_manager)
    assert isinstance(role_include, RoleInclude)

class MockAnsibleBaseYAMLObject(AnsibleBaseYAMLObject):
    def get(self, key, default=None):
        return getattr(self, key, default)

def test_role_include_load_valid_yaml_object_data(mock_loader, mock_variable_manager):
    play = object()
    data = MockAnsibleBaseYAMLObject()
    data.role = "valid_role"
    role_include = RoleInclude.load(data, play=play, loader=mock_loader, variable_manager=mock_variable_manager)
    assert isinstance(role_include, RoleInclude)
