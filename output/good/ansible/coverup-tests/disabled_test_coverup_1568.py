# file lib/ansible/playbook/role/definition.py:114-135
# lines [121, 122, 124, 125, 126, 130, 131, 132, 133, 135]
# branches ['121->122', '121->124', '125->126', '125->130', '130->131', '130->135']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from ansible.vars.manager import VariableManager

# Mock classes to avoid dependencies on Ansible internals
class MockLoader:
    def get_basedir(self):
        return './'

class MockPlay:
    pass

@pytest.fixture
def role_definition(mocker):
    # Create a RoleDefinition instance with mocks
    rd = RoleDefinition()
    rd._variable_manager = mocker.Mock(spec=VariableManager)
    rd._loader = MockLoader()
    rd._play = mocker.Mock(spec=MockPlay)
    return rd

def test_role_definition_with_string(role_definition):
    # Test with a string, should return the string itself
    role_name = "test_role"
    assert role_definition._load_role_name(role_name) == role_name

def test_role_definition_with_dict_no_name(role_definition):
    # Test with a dict without a role name, should raise AnsibleError
    with pytest.raises(AnsibleError):
        role_definition._load_role_name({})

def test_role_definition_with_dict_and_name(role_definition, mocker):
    # Test with a dict with a role name, should return the role name
    role_name = "test_role"
    ds = {'role': role_name}
    mocker.patch.object(Templar, 'template', return_value=role_name)
    mocker.patch.object(role_definition._variable_manager, 'get_vars', return_value={})
    assert role_definition._load_role_name(ds) == role_name

def test_role_definition_with_dict_and_templated_name(role_definition, mocker):
    # Test with a dict with a templated role name, should process and return the templated name
    role_name = "{{ role_var }}"
    templated_role_name = "templated_role"
    ds = {'role': role_name}
    mocker.patch.object(Templar, 'template', return_value=templated_role_name)
    mocker.patch.object(role_definition._variable_manager, 'get_vars', return_value={})
    assert role_definition._load_role_name(ds) == templated_role_name
