# file: lib/ansible/playbook/role/metadata.py:63-110
# asked: {"lines": [63, 69, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 87, 88, 90, 91, 94, 97, 98, 99, 100, 102, 103, 105, 106, 107, 108, 109, 110], "branches": [[70, 71], [70, 87], [71, 72], [71, 74], [74, 75], [74, 87], [75, 76], [75, 78], [81, 82], [81, 83], [90, 91], [90, 105], [98, 99], [98, 102], [102, 103], [102, 105]]}
# gained: {"lines": [63, 69, 70, 71, 72, 74, 75, 76, 77, 78, 80, 84, 85, 87, 88, 90, 91, 94, 97, 98, 99, 100, 102, 103, 105, 106, 107, 108, 109, 110], "branches": [[70, 71], [71, 72], [71, 74], [74, 75], [74, 87], [75, 76], [75, 78], [90, 91], [98, 99], [102, 103]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    owner = Mock()
    owner._role_path = "/path/to/role"
    owner.collections = ["ansible.collection1", "ansible.collection2"]
    owner._role_collection = "ansible.collection1"
    owner._play = Mock()
    variable_manager = Mock()
    loader = Mock()
    role_metadata_instance = RoleMetadata(owner=owner)
    role_metadata_instance._ds = Mock()  # Mocking _ds attribute
    return role_metadata_instance, variable_manager, loader

def test_load_dependencies_with_valid_list(role_metadata):
    role_metadata_instance, variable_manager, loader = role_metadata
    ds = [{"role": "test_role"}, {"name": "test_name"}]
    
    with patch("ansible.playbook.role.metadata.load_list_of_roles", return_value=["role1", "role2"]) as mock_load_roles:
        result = role_metadata_instance._load_dependencies("attr", ds)
        assert result == ["role1", "role2"]
        mock_load_roles.assert_called_once()

def test_load_dependencies_with_invalid_list(role_metadata):
    role_metadata_instance, variable_manager, loader = role_metadata
    ds = "invalid_string"
    
    with pytest.raises(AnsibleParserError, match="Expected role dependencies to be a list."):
        role_metadata_instance._load_dependencies("attr", ds)

def test_load_dependencies_with_role_error(role_metadata):
    role_metadata_instance, variable_manager, loader = role_metadata
    ds = [{"invalid_role_key": "value"}]
    
    with patch("ansible.playbook.role.metadata.RoleRequirement.role_yaml_parse", side_effect=AnsibleError("Role error")):
        with pytest.raises(AnsibleParserError, match="Role error"):
            role_metadata_instance._load_dependencies("attr", ds)

def test_load_dependencies_with_assertion_error(role_metadata):
    role_metadata_instance, variable_manager, loader = role_metadata
    ds = [{"role": "test_role"}]
    
    with patch("ansible.playbook.role.metadata.load_list_of_roles", side_effect=AssertionError("Assertion error")):
        with pytest.raises(AnsibleParserError, match="A malformed list of role dependencies was encountered."):
            role_metadata_instance._load_dependencies("attr", ds)
