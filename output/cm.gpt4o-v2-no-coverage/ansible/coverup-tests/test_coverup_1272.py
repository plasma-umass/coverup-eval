# file: lib/ansible/playbook/role/metadata.py:63-110
# asked: {"lines": [81, 82, 83], "branches": [[70, 87], [81, 82], [81, 83], [90, 105], [98, 102], [102, 105]]}
# gained: {"lines": [81, 82, 83], "branches": [[81, 82]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types
from ansible.playbook.helpers import load_list_of_roles
from ansible.playbook.role.requirement import RoleRequirement
from ansible.playbook.role.metadata import RoleMetadata
from ansible.playbook.role.include import RoleInclude

class TestRoleMetadata:

    @patch('ansible.playbook.role.metadata.load_list_of_roles')
    def test_load_dependencies_with_valid_roles(self, mock_load_list_of_roles):
        mock_load_list_of_roles.return_value = ['role1', 'role2']
        role_metadata = RoleMetadata()
        role_metadata._owner = MagicMock()
        role_metadata._owner._role_path = '/path/to/role'
        role_metadata._owner.collections = ['collection1']
        role_metadata._owner._role_collection = 'collection2'
        role_metadata._owner._play = MagicMock()
        role_metadata._variable_manager = MagicMock()
        role_metadata._loader = MagicMock()

        ds = [{'role': 'role1'}, {'name': 'role2'}]
        result = role_metadata._load_dependencies('attr', ds)
        assert result == ['role1', 'role2']
        mock_load_list_of_roles.assert_called_once()

    def test_load_dependencies_with_invalid_role_type(self):
        role_metadata = RoleMetadata()
        role_metadata._ds = 'invalid_ds'
        with pytest.raises(AnsibleParserError, match="Expected role dependencies to be a list."):
            role_metadata._load_dependencies('attr', 'invalid_ds')

    @patch('ansible.playbook.role.metadata.RoleRequirement.role_yaml_parse')
    @patch('ansible.playbook.role.metadata.load_list_of_roles')
    def test_load_dependencies_with_role_yaml_parse(self, mock_load_list_of_roles, mock_role_yaml_parse):
        mock_role_yaml_parse.return_value = {'name': 'parsed_role'}
        mock_load_list_of_roles.return_value = [RoleInclude()]
        role_metadata = RoleMetadata()
        role_metadata._owner = MagicMock()
        role_metadata._owner._role_path = '/path/to/role'
        role_metadata._owner.collections = ['collection1']
        role_metadata._owner._role_collection = 'collection2'
        role_metadata._owner._play = MagicMock()
        role_metadata._variable_manager = MagicMock()
        role_metadata._loader = MagicMock()

        ds = [{'src': 'galaxy.role,version,name'}]
        result = role_metadata._load_dependencies('attr', ds)
        assert isinstance(result[0], RoleInclude)
        mock_role_yaml_parse.assert_called_once()
        mock_load_list_of_roles.assert_called_once()

    @patch('ansible.playbook.role.metadata.load_list_of_roles')
    def test_load_dependencies_with_ansible_error(self, mock_load_list_of_roles):
        mock_load_list_of_roles.side_effect = AssertionError("Malformed list")
        role_metadata = RoleMetadata()
        role_metadata._ds = 'invalid_ds'
        role_metadata._owner = MagicMock()
        role_metadata._owner._role_path = '/path/to/role'
        role_metadata._owner.collections = ['collection1']
        role_metadata._owner._role_collection = 'collection2'
        role_metadata._owner._play = MagicMock()
        role_metadata._variable_manager = MagicMock()
        role_metadata._loader = MagicMock()

        ds = [{'role': 'role1'}, {'name': 'role2'}]
        with pytest.raises(AnsibleParserError, match="A malformed list of role dependencies was encountered."):
            role_metadata._load_dependencies('attr', ds)
