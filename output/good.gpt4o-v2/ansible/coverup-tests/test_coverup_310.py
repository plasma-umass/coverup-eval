# file: lib/ansible/playbook/role/definition.py:205-229
# asked: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}
# gained: {"lines": [205, 211, 212, 213, 214, 222, 224, 227, 229], "branches": [[214, 222], [214, 229], [222, 224], [222, 227]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition(mocker):
    mocker.patch.object(RoleDefinition, '_valid_attrs', {'_role': 'string'})
    return RoleDefinition()

def test_split_role_params(role_definition):
    ds = {
        'param1': 'value1',
        'param2': 'value2',
        '_role': 'test_role'
    }
    
    role_def, role_params = role_definition._split_role_params(ds)
    
    assert role_def == {'_role': 'test_role'}
    assert role_params == {'param1': 'value1', 'param2': 'value2'}
