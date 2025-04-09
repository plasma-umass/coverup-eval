# file lib/ansible/playbook/role/definition.py:205-229
# lines [205, 211, 212, 213, 214, 222, 224, 227, 229]
# branches ['214->222', '214->229', '222->224', '222->227']

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.utils.sentinel import Sentinel
from ansible.parsing.yaml.objects import AnsibleMapping
from ansible.module_utils.six import iteritems

# Mocking the Base class to simulate the _valid_attrs behavior
class MockBase:
    _valid_attrs = {
        'name': Sentinel,
        'vars': Sentinel
    }

# Inheriting from MockBase instead of Base to isolate the test environment
class MockRoleDefinition(MockBase, RoleDefinition):
    pass

@pytest.fixture
def role_definition():
    return MockRoleDefinition()

def test_split_role_params(role_definition):
    # Define a dataset that includes both valid attributes and extra params
    ds = {
        'name': 'test_role',
        'vars': {'var1': 'value1'},
        'extra_param1': 'value_extra1',
        'extra_param2': 'value_extra2',
        'tasks': [{'debug': {'msg': 'Hello world'}}]  # This should be treated as an extra param
    }

    # Convert to AnsibleMapping to simulate real Ansible input
    ds = AnsibleMapping(ds)

    # Call the method under test
    role_def, role_params = role_definition._split_role_params(ds)

    # Assertions to ensure the method is splitting the params correctly
    assert role_def == {
        'name': 'test_role',
        'vars': {'var1': 'value1'}
    }
    assert role_params == {
        'extra_param1': 'value_extra1',
        'extra_param2': 'value_extra2',
        'tasks': [{'debug': {'msg': 'Hello world'}}]  # This should be in role_params
    }

    # Clean up after the test
    del role_def
    del role_params
