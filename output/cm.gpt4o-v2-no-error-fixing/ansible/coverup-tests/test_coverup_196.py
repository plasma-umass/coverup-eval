# file: lib/ansible/playbook/role/definition.py:205-229
# asked: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}
# gained: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_split_role_params():
    role_def_instance = RoleDefinition()
    
    # Mocking _valid_attrs to simulate the environment
    role_def_instance._valid_attrs = {
        'name': 'some_value',
        'path': 'some_path'
    }
    
    ds = {
        'name': 'test_role',
        'path': '/some/path',
        'extra_param1': 'value1',
        'extra_param2': 'value2'
    }
    
    expected_role_def = {
        'name': 'test_role',
        'path': '/some/path'
    }
    
    expected_role_params = {
        'extra_param1': 'value1',
        'extra_param2': 'value2'
    }
    
    role_def, role_params = role_def_instance._split_role_params(ds)
    
    assert role_def == expected_role_def
    assert role_params == expected_role_params
