# file: lib/ansible/vars/hostvars.py:118-122
# asked: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from unittest.mock import MagicMock

from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    inventory.hosts = ['host1', 'host2']
    return inventory

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_hostvars_repr(hostvars, mock_inventory):
    # Mock the get method to return specific values for hosts
    hostvars.get = MagicMock(side_effect=lambda host: f"vars_for_{host}")

    # Call the __repr__ method
    result = repr(hostvars)

    # Verify the result
    expected_result = "{'host1': 'vars_for_host1', 'host2': 'vars_for_host2'}"
    assert result == expected_result

    # Verify that the get method was called for each host
    hostvars.get.assert_any_call('host1')
    hostvars.get.assert_any_call('host2')

    # Clean up
    hostvars.get.reset_mock()
