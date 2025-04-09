# file lib/ansible/playbook/role/metadata.py:63-110
# lines [69, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 87, 88, 90, 91, 94, 97, 98, 99, 100, 102, 103, 105, 106, 107, 108, 109, 110]
# branches ['70->71', '70->87', '71->72', '71->74', '74->75', '74->87', '75->76', '75->78', '81->82', '81->83', '90->91', '90->105', '98->99', '98->102', '102->103', '102->105']

import os
import pytest
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.playbook.role.metadata import RoleMetadata
from ansible.playbook.role.include import RoleInclude
from ansible.module_utils._text import to_native
from ansible.playbook.role.requirement import RoleRequirement

# Mocking string_types for compatibility with the provided code snippet
string_types = (str,)

# Mocking the load_list_of_roles function
def mock_load_list_of_roles(roles, play, current_role_path, variable_manager, loader, collection_search_list):
    # Simulate an AssertionError for malformed role definitions
    for role_def in roles:
        if not isinstance(role_def, (string_types, dict)) or 'invalid' in role_def:
            raise AssertionError("Malformed role definition")
    return [RoleInclude(role_def) for role_def in roles]

# Mocking the Base class
class Base:
    def __init__(self):
        pass

# Mocking the AnsibleParserError class
class AnsibleParserError(Exception):
    def __init__(self, message, obj=None, orig_exc=None):
        super().__init__(message)
        self.obj = obj
        self.orig_exc = orig_exc

# Mocking the AnsibleError class
class AnsibleError(Exception):
    pass

# Mocking the RoleRequirement class
class RoleRequirement:
    @staticmethod
    def role_yaml_parse(role_def):
        if 'src' in role_def:
            return {'name': role_def['src']}
        return {}

# Mocking the CollectionSearch class
class CollectionSearch:
    pass

@pytest.fixture
def mock_role_metadata(mocker):
    mocker.patch('ansible.playbook.role.metadata.load_list_of_roles', side_effect=mock_load_list_of_roles)
    mocker.patch('ansible.playbook.role.metadata.RoleRequirement', RoleRequirement)
    mocker.patch('ansible.playbook.role.metadata.string_types', string_types)
    mocker.patch('ansible.playbook.role.metadata.AnsibleParserError', AnsibleParserError)
    mocker.patch('ansible.playbook.role.metadata.AnsibleError', AnsibleError)
    mocker.patch('ansible.playbook.role.metadata.Base', Base)
    mocker.patch('ansible.playbook.role.metadata.CollectionSearch', CollectionSearch)
    return RoleMetadata()

def test_load_dependencies(mock_role_metadata, mocker):
    # Test with a valid list of dependencies
    dependencies = [
        'role1',
        {'role': 'role2'},
        {'name': 'role3'},
        {'src': 'galaxy.role,version,name'}
    ]
    mock_role_metadata._owner = mocker.Mock()
    mock_role_metadata._owner._role_path = '/path/to/role'
    mock_role_metadata._owner._play = mocker.Mock()
    mock_role_metadata._owner._role_collection = 'my_collection'
    mock_role_metadata._owner.collections = ['collection1', 'collection2']
    mock_role_metadata._variable_manager = mocker.Mock()
    mock_role_metadata._loader = mocker.Mock()
    mock_role_metadata._ds = dependencies

    result = mock_role_metadata._load_dependencies('dependencies', dependencies)
    assert len(result) == 4
    assert all(isinstance(role, RoleInclude) for role in result)

    # Test with a non-list dependencies
    with pytest.raises(AnsibleParserError) as exc_info:
        mock_role_metadata._load_dependencies('dependencies', 'not a list')
    assert "Expected role dependencies to be a list." in str(exc_info.value)

    # Test with a malformed role definition
    malformed_dependencies = [{'invalid': 'role'}]
    with pytest.raises(AnsibleParserError) as exc_info:
        mock_role_metadata._load_dependencies('dependencies', malformed_dependencies)
    assert "A malformed list of role dependencies was encountered." in str(exc_info.value)

    # Test with an AnsibleError during role parsing
    mocker.patch('ansible.playbook.role.metadata.RoleRequirement.role_yaml_parse', side_effect=AnsibleError('parsing error'))
    with pytest.raises(AnsibleParserError) as exc_info:
        mock_role_metadata._load_dependencies('dependencies', [{'src': 'galaxy.role,version,name'}])
    assert "parsing error" in str(exc_info.value)
