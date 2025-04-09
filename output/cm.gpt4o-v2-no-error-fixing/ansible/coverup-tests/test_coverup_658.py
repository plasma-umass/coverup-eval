# file: lib/ansible/vars/hostvars.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, variable_manager, loader)

def test_set_nonpersistent_facts(hostvars):
    host = 'test_host'
    facts = {'fact1': 'value1'}

    hostvars.set_nonpersistent_facts(host, facts)

    hostvars._variable_manager.set_nonpersistent_facts.assert_called_once_with(host, facts)
