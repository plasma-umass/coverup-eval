# file: lib/ansible/vars/hostvars.py:107-109
# asked: {"lines": [107, 109], "branches": []}
# gained: {"lines": [107, 109], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_hostvars_contains_existing_host(hostvars, mock_inventory):
    mock_inventory.get_host.return_value = True
    assert 'existing_host' in hostvars
    mock_inventory.get_host.assert_called_once_with('existing_host')

def test_hostvars_contains_non_existing_host(hostvars, mock_inventory):
    mock_inventory.get_host.return_value = None
    assert 'non_existing_host' not in hostvars
    mock_inventory.get_host.assert_called_once_with('non_existing_host')
