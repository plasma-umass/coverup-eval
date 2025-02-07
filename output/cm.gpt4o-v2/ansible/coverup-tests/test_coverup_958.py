# file: lib/ansible/vars/hostvars.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def hostvars(mock_variable_manager):
    inventory = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, mock_variable_manager, loader)

def test_set_host_facts(hostvars, mock_variable_manager):
    host = 'test_host'
    facts = {'fact1': 'value1'}

    hostvars.set_host_facts(host, facts)

    mock_variable_manager.set_host_facts.assert_called_once_with(host, facts)
