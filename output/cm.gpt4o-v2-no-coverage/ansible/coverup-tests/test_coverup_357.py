# file: lib/ansible/playbook/role/definition.py:205-229
# asked: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}
# gained: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition
from unittest.mock import MagicMock

@pytest.fixture
def role_definition():
    # Mocking the _valid_attrs attribute
    role_def = RoleDefinition()
    role_def._valid_attrs = {
        'name': 'some_name',
        'path': 'some_path'
    }
    return role_def

def test_split_role_params_with_valid_attrs(role_definition):
    ds = {
        'name': 'test_role',
        'path': '/some/path',
        'extra_param': 'value'
    }
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'name': 'test_role', 'path': '/some/path'}
    assert role_params == {'extra_param': 'value'}

def test_split_role_params_with_only_valid_attrs(role_definition):
    ds = {
        'name': 'test_role',
        'path': '/some/path'
    }
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'name': 'test_role', 'path': '/some/path'}
    assert role_params == {}

def test_split_role_params_with_only_extra_params(role_definition):
    ds = {
        'extra_param1': 'value1',
        'extra_param2': 'value2'
    }
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {}
    assert role_params == {'extra_param1': 'value1', 'extra_param2': 'value2'}
