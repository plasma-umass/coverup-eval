# file: lib/ansible/vars/hostvars.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    variable_manager = MagicMock()
    inventory = MagicMock()
    loader = MagicMock()
    return HostVars(variable_manager=variable_manager, inventory=inventory, loader=loader)

def test_set_host_facts(hostvars):
    host = 'test_host'
    facts = {'fact1': 'value1', 'fact2': 'value2'}
    
    hostvars.set_host_facts(host, facts)
    
    hostvars._variable_manager.set_host_facts.assert_called_once_with(host, facts)
