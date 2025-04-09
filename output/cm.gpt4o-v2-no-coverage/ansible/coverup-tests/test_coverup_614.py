# file: lib/ansible/vars/hostvars.py:118-122
# asked: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    class MockInventory:
        def __init__(self):
            self.hosts = ['host1', 'host2']
    return MockInventory()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_hostvars_repr(hostvars, mock_inventory, monkeypatch):
    def mock_get(host):
        return f"vars_for_{host}"
    
    monkeypatch.setattr(hostvars, 'get', mock_get)
    
    expected_repr = "{'host1': 'vars_for_host1', 'host2': 'vars_for_host2'}"
    assert repr(hostvars) == expected_repr
