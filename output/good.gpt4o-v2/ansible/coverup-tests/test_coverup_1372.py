# file: lib/ansible/playbook/role/definition.py:114-135
# asked: {"lines": [124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}
# gained: {"lines": [124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 124], [125, 126], [125, 130], [130, 131]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
from ansible.template import Templar
from ansible.playbook.role.definition import RoleDefinition

class MockVariableManager:
    def get_vars(self, play):
        return {'var_role_name': 'templated_role_name'}

class MockLoader:
    def get_basedir(self):
        return './'

class MockPlay:
    pass

@pytest.fixture
def role_definition():
    return RoleDefinition(
        play=MockPlay(),
        variable_manager=MockVariableManager(),
        loader=MockLoader()
    )

def test_load_role_name_with_string(role_definition):
    ds = 'simple_role_name'
    result = role_definition._load_role_name(ds)
    assert result == 'simple_role_name'

def test_load_role_name_with_dict(role_definition):
    ds = {'role': 'dict_role_name'}
    result = role_definition._load_role_name(ds)
    assert result == 'dict_role_name'

def test_load_role_name_with_name_key(role_definition):
    ds = {'name': 'dict_name_key'}
    result = role_definition._load_role_name(ds)
    assert result == 'dict_name_key'

def test_load_role_name_with_missing_role_name(role_definition):
    ds = {'invalid_key': 'value'}
    with pytest.raises(AnsibleError, match='role definitions must contain a role name'):
        role_definition._load_role_name(ds)

def test_load_role_name_with_templating(role_definition, monkeypatch):
    ds = {'role': 'role_with_{{ var_role_name }}'}
    result = role_definition._load_role_name(ds)
    assert result == 'role_with_templated_role_name'
