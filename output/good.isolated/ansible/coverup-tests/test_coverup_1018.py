# file lib/ansible/vars/hostvars.py:101-102
# lines [101, 102]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def variable_manager(mocker):
    return mocker.MagicMock(spec=VariableManager)

@pytest.fixture
def data_loader(mocker):
    return mocker.MagicMock(spec=DataLoader)

@pytest.fixture
def inventory_manager(mocker):
    return mocker.MagicMock(spec=InventoryManager)

@pytest.fixture
def hostvars(variable_manager, data_loader, inventory_manager):
    return HostVars(inventory=inventory_manager, variable_manager=variable_manager, loader=data_loader)

def test_set_nonpersistent_facts(hostvars, variable_manager):
    host = 'testhost'
    facts = {'key': 'value'}
    
    hostvars.set_nonpersistent_facts(host, facts)
    
    variable_manager.set_nonpersistent_facts.assert_called_once_with(host, facts)
