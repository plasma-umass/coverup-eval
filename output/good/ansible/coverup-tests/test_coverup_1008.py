# file lib/ansible/vars/hostvars.py:104-105
# lines [104, 105]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock, create_autospec

@pytest.fixture
def variable_manager():
    return create_autospec(VariableManager)

@pytest.fixture
def data_loader():
    return create_autospec(DataLoader)

@pytest.fixture
def inventory():
    return MagicMock()

@pytest.fixture
def hostvars(variable_manager, data_loader, inventory):
    return HostVars(inventory, variable_manager, data_loader)

def test_set_host_facts(hostvars, variable_manager):
    host = 'test_host'
    facts = {'key': 'value'}

    hostvars.set_host_facts(host, facts)

    # Verify that set_host_facts calls the VariableManager's set_host_facts with correct parameters
    variable_manager.set_host_facts.assert_called_once_with(host, facts)
