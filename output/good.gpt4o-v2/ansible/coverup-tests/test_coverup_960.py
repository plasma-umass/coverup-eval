# file: lib/ansible/vars/hostvars.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return Mock()

@pytest.fixture
def hostvars(mock_variable_manager):
    inventory = Mock()
    loader = Mock()
    return HostVars(inventory, mock_variable_manager, loader)

def test_set_nonpersistent_facts(hostvars, mock_variable_manager):
    host = 'test_host'
    facts = {'fact1': 'value1'}

    hostvars.set_nonpersistent_facts(host, facts)

    mock_variable_manager.set_nonpersistent_facts.assert_called_once_with(host, facts)
