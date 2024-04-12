# file lib/ansible/playbook/role/definition.py:114-135
# lines [122]
# branches ['121->122', '130->135']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from ansible.utils.sentinel import Sentinel
from ansible.vars.manager import VariableManager

# Mock classes to avoid side effects
class MockLoader:
    def get_basedir(self):
        return './'

class MockPlay:
    pass

@pytest.fixture
def role_definition(mocker):
    # Setup the RoleDefinition with mocks
    variable_manager = mocker.MagicMock(spec=VariableManager)
    loader = MockLoader()
    play = mocker.MagicMock(spec=MockPlay)
    rd = RoleDefinition()
    rd._variable_manager = variable_manager
    rd._loader = loader
    rd._play = play
    return rd

def test_role_definition_with_string(role_definition):
    # Test with a string, should return the string itself
    role_string = 'test_role'
    assert role_definition._load_role_name(role_string) == role_string

def test_role_definition_with_variables(role_definition, mocker):
    # Test with a variable in the role name, should template it
    role_with_vars = {'role': '{{ role_var }}'}
    expected_role_name = 'templated_role'
    all_vars = {'role_var': 'templated_role'}

    # Mock the methods and variables to return expected values
    role_definition._variable_manager.get_vars.return_value = all_vars
    mocker.patch.object(Templar, 'template', return_value=expected_role_name)

    assert role_definition._load_role_name(role_with_vars) == expected_role_name
    Templar.template.assert_called_once_with('{{ role_var }}')

def test_role_definition_without_role_name(role_definition):
    # Test with a missing role name, should raise AnsibleError
    role_without_name = {'not_a_role': 'some_value'}
    with pytest.raises(AnsibleError):
        role_definition._load_role_name(role_without_name)

def test_role_definition_with_non_string_name(role_definition):
    # Test with a non-string role name, should raise AnsibleError
    role_with_non_string_name = {'role': 123}
    with pytest.raises(AnsibleError):
        role_definition._load_role_name(role_with_non_string_name)
