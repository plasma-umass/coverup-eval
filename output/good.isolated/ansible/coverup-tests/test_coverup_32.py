# file lib/ansible/playbook/role/definition.py:137-203
# lines [137, 147, 148, 150, 152, 153, 155, 158, 159, 161, 163, 164, 171, 172, 176, 177, 181, 182, 187, 190, 191, 192, 193, 194, 197, 198, 199, 200, 202, 203]
# branches ['147->148', '147->150', '158->159', '158->161', '161->163', '161->171', '176->177', '176->181', '181->182', '181->187', '190->191', '190->197', '193->190', '193->194', '198->199', '198->202']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from ansible.utils.collection_loader import AnsibleCollectionRef
from ansible.utils.path import unfrackpath
from ansible import constants as C

# Mocking the necessary parts of the Ansible codebase that are not provided
class Base:
    pass

class Conditional:
    pass

class Taggable:
    pass

class CollectionSearch:
    pass

class MockLoader:
    def get_basedir(self):
        return '/fake/base/dir'

    def path_exists(self, path):
        return False

class MockVariableManager:
    def get_vars(self, play=None):
        return {}

@pytest.fixture
def mock_loader(mocker):
    return mocker.Mock(spec=MockLoader)

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.Mock(spec=MockVariableManager)

@pytest.fixture
def role_definition(mock_loader, mock_variable_manager):
    rd = RoleDefinition()
    rd._loader = mock_loader
    rd._variable_manager = mock_variable_manager
    rd._play = None
    rd._role_basedir = None
    rd._collection_list = None
    rd._ds = None  # Add this line to set the _ds attribute
    return rd

def test_role_definition_not_found_error(role_definition, mocker):
    role_name = "non_existent_role"
    mocker.patch.object(role_definition._loader, 'get_basedir', return_value='/fake/base/dir')
    mocker.patch.object(role_definition._loader, 'path_exists', return_value=False)
    mocker.patch.object(Templar, 'template', side_effect=lambda x: x)
    mocker.patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=False)
    mocker.patch.object(C, 'DEFAULT_ROLES_PATH', ['/etc/ansible/roles'])

    with pytest.raises(AnsibleError) as excinfo:
        role_definition._load_role_path(role_name)

    expected_error_msg = "the role 'non_existent_role' was not found in /fake/base/dir/roles:/etc/ansible/roles:/fake/base/dir"
    assert str(excinfo.value) == expected_error_msg
