# file: lib/ansible/vars/hostvars.py:111-113
# asked: {"lines": [111, 112, 113], "branches": [[112, 0], [112, 113]]}
# gained: {"lines": [111, 112, 113], "branches": [[112, 0], [112, 113]]}

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

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_hostvars_iter(hostvars):
    hosts = list(hostvars)
    assert hosts == ['host1', 'host2', 'host3']
