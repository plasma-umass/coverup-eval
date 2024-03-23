# file lib/ansible/playbook/role/definition.py:137-203
# lines [147, 148, 150, 152, 153, 155, 158, 159, 161, 163, 164, 171, 172, 176, 177, 181, 182, 187, 190, 191, 192, 193, 194, 197, 198, 199, 200, 202, 203]
# branches ['147->148', '147->150', '158->159', '158->161', '161->163', '161->171', '176->177', '176->181', '181->182', '181->187', '190->191', '190->197', '193->190', '193->194', '198->199', '198->202']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from ansible.utils.path import unfrackpath
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.utils.collection_loader import AnsibleCollectionRef

# Mock configuration constant
class C:
    DEFAULT_ROLES_PATH = []

# Mock function to simulate collection role path retrieval
def _get_collection_role_path(role_name, collection_list):
    return None

# Test function to cover lines 147-203
def test_role_definition_load_role_path(mocker):
    # Mock necessary components
    variable_manager = mocker.MagicMock(spec=VariableManager)
    variable_manager.get_vars.return_value = {}
    loader = mocker.MagicMock(spec=DataLoader)
    loader.get_basedir.return_value = '/fake/playbook/dir'
    loader.path_exists.return_value = False
    play = mocker.MagicMock(spec=Play)
    ds = mocker.MagicMock()  # Mock the data structure that would be passed to RoleDefinition

    # Create a RoleDefinition instance with mocks
    role_def = RoleDefinition()
    role_def._variable_manager = variable_manager
    role_def._loader = loader
    role_def._play = play
    role_def._role_basedir = '/fake/roles/basedir'
    role_def._collection_list = []
    role_def._ds = ds  # Set the mocked data structure

    # Mock the _get_collection_role_path to return None
    mocker.patch('ansible.playbook.role.definition._get_collection_role_path', _get_collection_role_path)

    # Test with a role name that does not exist
    with pytest.raises(AnsibleError) as excinfo:
        role_def._load_role_path('non_existent_role')

    # Verify the exception message
    assert "the role 'non_existent_role' was not found in" in str(excinfo.value)

    # Test with a role name that exists as a directory
    loader.path_exists.return_value = True
    role_name, role_path = role_def._load_role_path('existent_role')
    assert role_name == 'existent_role'
    assert role_path.startswith('/fake/playbook/dir/roles/existent_role')

    # Cleanup after test
    mocker.stopall()
