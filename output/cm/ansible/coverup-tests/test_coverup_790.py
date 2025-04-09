# file lib/ansible/vars/manager.py:139-141
# lines [139, 140, 141]
# branches []

import pytest
from ansible.vars.manager import VariableManager

# Test function to cover the extra_vars property
def test_extra_vars_property():
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'test_key': 'test_value'}

    # Access the property to ensure the code is executed
    extra_vars = variable_manager.extra_vars

    # Assert that the property returns the correct value
    assert extra_vars == {'test_key': 'test_value'}

# Fixture to mock VariableManager for isolation
@pytest.fixture
def variable_manager(mocker):
    variable_manager_instance = VariableManager()
    mocker.patch.object(variable_manager_instance, '_extra_vars', new_callable=mocker.PropertyMock(return_value={'mocked_key': 'mocked_value'}))
    return variable_manager_instance

# Test function using the fixture
def test_extra_vars_property_with_fixture(variable_manager):
    # Access the property to ensure the code is executed
    extra_vars = variable_manager.extra_vars

    # Assert that the property returns the mocked value
    assert extra_vars == {'mocked_key': 'mocked_value'}
