# file lib/ansible/playbook/role/definition.py:205-229
# lines [205, 211, 212, 213, 214, 222, 224, 227, 229]
# branches ['214->222', '214->229', '222->224', '222->227']

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.utils.vars import merge_hash

class MockBase:
    _valid_attrs = {'name': None, 'src': None}

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestRoleDefinition(MockBase, MockConditional, MockTaggable, MockCollectionSearch, RoleDefinition):
    def __init__(self):
        self._valid_attrs = MockBase._valid_attrs

@pytest.fixture
def role_definition():
    return TestRoleDefinition()

def test_split_role_params(role_definition):
    ds = {
        'name': 'test_role',
        'src': 'some_source',
        'extra_param1': 'value1',
        'extra_param2': 'value2'
    }
    
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'name': 'test_role', 'src': 'some_source'}
    assert role_params == {'extra_param1': 'value1', 'extra_param2': 'value2'}
