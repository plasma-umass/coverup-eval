# file: lib/ansible/playbook/role/definition.py:114-135
# asked: {"lines": [114, 121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}
# gained: {"lines": [114, 121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar

class MockVariableManager:
    def get_vars(self, play):
        return {"role_var": "templated_role"}

class MockLoader:
    def get_basedir(self):
        return "mock_basedir"

@pytest.fixture
def role_definition():
    return RoleDefinition(
        play="mock_play",
        role_basedir="mock_basedir",
        variable_manager=MockVariableManager(),
        loader=MockLoader()
    )

def test_load_role_name_with_string(role_definition):
    assert role_definition._load_role_name("simple_role") == "simple_role"

def test_load_role_name_with_dict(role_definition):
    ds = {"role": "complex_role"}
    assert role_definition._load_role_name(ds) == "complex_role"

def test_load_role_name_with_name_field(role_definition):
    ds = {"name": "name_field_role"}
    assert role_definition._load_role_name(ds) == "name_field_role"

def test_load_role_name_with_missing_role_name(role_definition):
    ds = {"invalid_key": "value"}
    with pytest.raises(AnsibleError, match="role definitions must contain a role name"):
        role_definition._load_role_name(ds)

def test_load_role_name_with_templating(role_definition, mocker):
    ds = {"role": "{{ role_var }}_role"}
    mocker.patch.object(Templar, 'template', return_value="templated_role")
    assert role_definition._load_role_name(ds) == "templated_role"
