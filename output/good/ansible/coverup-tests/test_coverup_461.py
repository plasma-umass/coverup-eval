# file lib/ansible/inventory/group.py:244-252
# lines [244, 246, 247, 249, 250, 252]
# branches ['246->247', '246->249', '249->250', '249->252']

import pytest
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars
from collections.abc import MutableMapping

# Mocking the combine_vars function to ensure it is called without executing its logic
@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.inventory.group.combine_vars', return_value={'some_key': {'inner_key': 'inner_value', 'another_key': 'another_value'}})

# Test function to cover the missing branch where both self.vars[key] and value are mappings
def test_set_variable_with_mappings(mock_combine_vars):
    group = Group()
    group.vars = {'some_key': {'inner_key': 'inner_value'}}
    new_value = {'another_key': 'another_value'}

    # Set a variable where the key is not 'ansible_group_priority' and both values are mappings
    group.set_variable('some_key', new_value)

    # Assert combine_vars was called with the correct parameters
    mock_combine_vars.assert_called_once_with({'some_key': {'inner_key': 'inner_value'}}, {'some_key': new_value})

    # Assert that combine_vars result is correctly assigned to group.vars
    assert group.vars['some_key'] == {'inner_key': 'inner_value', 'another_key': 'another_value'}

# Test function to cover the missing branch where self.vars[key] is not a mapping or value is not a mapping
def test_set_variable_with_non_mappings():
    group = Group()
    group.vars = {'some_key': 'some_value'}
    new_value = 'new_value'

    # Set a variable where the key is not 'ansible_group_priority' and at least one value is not a mapping
    group.set_variable('some_key', new_value)

    # Assert the value was set correctly
    assert group.vars['some_key'] == new_value
