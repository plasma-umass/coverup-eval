# file lib/ansible/playbook/role/definition.py:205-229
# lines [211, 212, 213, 214, 222, 224, 227, 229]
# branches ['214->222', '214->229', '222->224', '222->227']

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    return RoleDefinition()

def test_split_role_params(role_definition, mocker):
    # Mocking iteritems to return a dictionary that contains keys both in and out of _valid_attrs
    mocker.patch('ansible.playbook.role.definition.iteritems', return_value=[('valid_key', 'valid_value'), ('extra_key', 'extra_value')])
    mocker.patch.object(role_definition, '_valid_attrs', {'valid_key': None})

    # Call the method under test
    role_def, role_params = role_definition._split_role_params({})

    # Assertions to check if the method separates the parameters correctly
    assert 'valid_key' in role_def
    assert role_def['valid_key'] == 'valid_value'
    assert 'extra_key' in role_params
    assert role_params['extra_key'] == 'extra_value'

    # Clean up the mocker
    mocker.stopall()
