# file lib/ansible/playbook/role/definition.py:114-135
# lines [114, 121, 122, 124, 125, 126, 130, 131, 132, 133, 135]
# branches ['121->122', '121->124', '125->126', '125->130', '130->131', '130->135']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play

# Mock classes to avoid side effects
class MockVariableManager(VariableManager):
    def get_vars(self, play=None):
        return {}

class MockLoader(DataLoader):
    pass

@pytest.fixture
def role_definition(mocker):
    # Mock the VariableManager and DataLoader to avoid side effects
    variable_manager = MockVariableManager()
    loader = MockLoader()
    play = Play()

    # Create a RoleDefinition instance with mocks
    role_def = RoleDefinition()
    role_def._variable_manager = variable_manager
    role_def._loader = loader
    role_def._play = play

    return role_def

def test_role_definition_with_invalid_name(role_definition):
    with pytest.raises(AnsibleError) as excinfo:
        role_definition._load_role_name({'name': 123})
    assert 'role definitions must contain a role name' in str(excinfo.value)

def test_role_definition_with_variable_name(role_definition, mocker):
    # Mock the Templar to return a templated name
    mocker.patch.object(Templar, 'template', return_value='templated_role_name')

    role_name = role_definition._load_role_name({'name': '{{ role_var }}'})
    assert role_name == 'templated_role_name'
    Templar.template.assert_called_once()
