# file lib/ansible/playbook/role/metadata.py:63-110
# lines [63, 69, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 87, 88, 90, 91, 94, 97, 98, 99, 100, 102, 103, 105, 106, 107, 108, 109, 110]
# branches ['70->71', '70->87', '71->72', '71->74', '74->75', '74->87', '75->76', '75->78', '81->82', '81->83', '90->91', '90->105', '98->99', '98->102', '102->103', '102->105']

import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.module_utils._text import to_native
from unittest.mock import MagicMock, patch

def test_load_dependencies_with_invalid_ds():
    role_metadata = RoleMetadata()
    role_metadata._ds = "dummy_ds"
    
    with pytest.raises(AnsibleParserError, match="Expected role dependencies to be a list."):
        role_metadata._load_dependencies('dependencies', 'not_a_list')

def test_load_dependencies_with_valid_ds(mocker):
    role_metadata = RoleMetadata()
    role_metadata._ds = "dummy_ds"
    role_metadata._owner = MagicMock()
    role_metadata._owner._role_path = "/path/to/role"
    role_metadata._owner.collections = ['ansible.collection1']
    role_metadata._owner._role_collection = 'ansible.collection2'
    role_metadata._owner._play = MagicMock()
    role_metadata._variable_manager = MagicMock()
    role_metadata._loader = MagicMock()

    mocker.patch('ansible.playbook.role.metadata.load_list_of_roles', return_value=['role1', 'role2'])
    mocker.patch('ansible.playbook.role.metadata.RoleRequirement.role_yaml_parse', return_value={'name': 'parsed_role'})

    ds = [{'role': 'role1'}, {'name': 'role2'}, {'src': 'galaxy.role,version,name'}]
    result = role_metadata._load_dependencies('dependencies', ds)

    assert result == ['role1', 'role2']
    assert role_metadata._owner.collections == ['ansible.collection1']
    assert role_metadata._owner._role_collection == 'ansible.collection2'

def test_load_dependencies_with_ansible_error(mocker):
    role_metadata = RoleMetadata()
    role_metadata._ds = "dummy_ds"
    
    mocker.patch('ansible.playbook.role.metadata.RoleRequirement.role_yaml_parse', side_effect=AnsibleError("An error occurred"))
    
    ds = [{'src': 'galaxy.role,version,name'}]
    
    with pytest.raises(AnsibleParserError, match="An error occurred"):
        role_metadata._load_dependencies('dependencies', ds)

def test_load_dependencies_with_assertion_error(mocker):
    role_metadata = RoleMetadata()
    role_metadata._ds = "dummy_ds"
    role_metadata._owner = MagicMock()
    role_metadata._owner._role_path = "/path/to/role"
    role_metadata._owner.collections = ['ansible.collection1']
    role_metadata._owner._role_collection = 'ansible.collection2'
    role_metadata._owner._play = MagicMock()
    role_metadata._variable_manager = MagicMock()
    role_metadata._loader = MagicMock()

    mocker.patch('ansible.playbook.role.metadata.load_list_of_roles', side_effect=AssertionError("Malformed list"))

    ds = [{'role': 'role1'}, {'name': 'role2'}, {'src': 'galaxy.role,version,name'}]
    
    with pytest.raises(AnsibleParserError, match="A malformed list of role dependencies was encountered."):
        role_metadata._load_dependencies('dependencies', ds)
