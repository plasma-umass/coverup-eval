# file: lib/ansible/inventory/manager.py:605-615
# asked: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}
# gained: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import Mock
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_manager():
    loader = Mock()
    return InventoryManager(loader)

def test_restrict_to_hosts_none(inventory_manager):
    inventory_manager.restrict_to_hosts(None)
    assert inventory_manager._restriction is None

def test_restrict_to_hosts_not_list(inventory_manager):
    host = Mock()
    host.name = 'host1'
    inventory_manager.restrict_to_hosts(host)
    assert inventory_manager._restriction == {to_text('host1')}

def test_restrict_to_hosts_list(inventory_manager):
    host1 = Mock()
    host1.name = 'host1'
    host2 = Mock()
    host2.name = 'host2'
    inventory_manager.restrict_to_hosts([host1, host2])
    assert inventory_manager._restriction == {to_text('host1'), to_text('host2')}
