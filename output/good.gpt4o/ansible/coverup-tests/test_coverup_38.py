# file lib/ansible/playbook/role/definition.py:137-203
# lines [137, 147, 148, 150, 152, 153, 155, 158, 159, 161, 163, 164, 171, 172, 176, 177, 181, 182, 187, 190, 191, 192, 193, 194, 197, 198, 199, 200, 202, 203]
# branches ['147->148', '147->150', '158->159', '158->161', '161->163', '161->171', '176->177', '176->181', '181->182', '181->187', '190->191', '190->197', '193->190', '193->194', '198->199', '198->202']

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError

@pytest.fixture
def mock_loader():
    loader = MagicMock()
    loader.get_basedir.return_value = '/mock_basedir'
    loader.path_exists.side_effect = lambda x: x in [
        '/mock_basedir/roles/role1',
        '/mock_basedir/roles/role2',
        '/mock_basedir/role3'
    ]
    return loader

@pytest.fixture
def mock_variable_manager():
    variable_manager = MagicMock()
    variable_manager.get_vars.return_value = {'var1': 'value1'}
    return variable_manager

@pytest.fixture
def role_definition(mock_loader, mock_variable_manager):
    role_def = RoleDefinition()
    role_def._loader = mock_loader
    role_def._variable_manager = mock_variable_manager
    role_def._play = MagicMock()
    role_def._collection_list = None
    role_def._role_basedir = None
    role_def._ds = MagicMock()
    return role_def

def test_load_role_path_collection_role(role_definition):
    with patch('ansible.playbook.role.definition._get_collection_role_path') as mock_get_collection_role_path, \
         patch('ansible.playbook.role.definition.AnsibleCollectionRef.is_valid_fqcr', return_value=True):
        mock_get_collection_role_path.return_value = ('role_name', 'role_path', 'role_collection')
        role_name, role_path = role_definition._load_role_path('role_name')
        assert role_name == 'role_name'
        assert role_path == 'role_path'
        assert role_definition._role_collection == 'role_collection'

def test_load_role_path_defined_role_paths(role_definition):
    role_definition._role_basedir = '/mock_role_basedir'
    role_name, role_path = role_definition._load_role_path('role1')
    assert role_name == 'role1'
    assert role_path == '/mock_basedir/roles/role1'

def test_load_role_path_current_basedir(role_definition):
    role_name, role_path = role_definition._load_role_path('role3')
    assert role_name == 'role3'
    assert role_path == '/mock_basedir/role3'

def test_load_role_path_not_found(role_definition):
    with pytest.raises(AnsibleError, match="the role 'nonexistent_role' was not found"):
        role_definition._load_role_path('nonexistent_role')
