# file lib/ansible/vars/hostvars.py:101-102
# lines [102]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    hv = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    return hv

def test_set_nonpersistent_facts(hostvars, mock_variable_manager):
    host = 'test_host'
    facts = {'fact1': 'value1', 'fact2': 'value2'}
    
    hostvars.set_nonpersistent_facts(host, facts)
    
    mock_variable_manager.set_nonpersistent_facts.assert_called_once_with(host, facts)
