# file lib/ansible/vars/hostvars.py:118-122
# lines [119, 120, 121, 122]
# branches ['120->121', '120->122']

import pytest
from unittest.mock import MagicMock

# Assuming the HostVars class is imported from ansible.vars.hostvars
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
    hv = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    return hv

def test_hostvars_repr(hostvars, mocker):
    # Mock the get method to return specific values for hosts
    mocker.patch.object(hostvars, 'get', side_effect=lambda host: f"vars_for_{host}")

    # Call the __repr__ method to ensure lines 119-122 are executed
    result = repr(hostvars)

    # Verify the result
    expected_result = repr({'host1': 'vars_for_host1', 'host2': 'vars_for_host2'})
    assert result == expected_result

    # Clean up
    mocker.stopall()
