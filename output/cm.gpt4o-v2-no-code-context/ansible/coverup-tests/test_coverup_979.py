# file: lib/ansible/playbook/role/definition.py:205-229
# asked: {"lines": [211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}
# gained: {"lines": [211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    return RoleDefinition()

def test_split_role_params_with_field_attributes(role_definition):
    ds = {
        'name': 'test_role',
        'src': 'some_source',
        'version': '1.0',
    }
    role_definition._valid_attrs = {
        'name': None,
        'src': None,
    }
    
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'name': 'test_role', 'src': 'some_source'}
    assert role_params == {'version': '1.0'}

def test_split_role_params_with_only_role_params(role_definition):
    ds = {
        'param1': 'value1',
        'param2': 'value2',
    }
    role_definition._valid_attrs = {
        'name': None,
        'src': None,
    }
    
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {}
    assert role_params == {'param1': 'value1', 'param2': 'value2'}

def test_split_role_params_with_mixed_attributes(role_definition):
    ds = {
        'name': 'test_role',
        'param1': 'value1',
        'src': 'some_source',
        'param2': 'value2',
    }
    role_definition._valid_attrs = {
        'name': None,
        'src': None,
    }
    
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'name': 'test_role', 'src': 'some_source'}
    assert role_params == {'param1': 'value1', 'param2': 'value2'}
