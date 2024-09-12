# file: lib/ansible/vars/hostvars.py:115-116
# asked: {"lines": [115, 116], "branches": []}
# gained: {"lines": [115, 116], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    inventory.hosts = ['host1', 'host2', 'host3']
    return inventory

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

def test_hostvars_len(mock_inventory, mock_variable_manager, mock_loader):
    hostvars = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    assert len(hostvars) == 3
