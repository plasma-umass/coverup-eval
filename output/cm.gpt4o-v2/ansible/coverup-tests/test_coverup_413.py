# file: lib/ansible/inventory/manager.py:605-615
# asked: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}
# gained: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.host import Host
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=None)

def test_restrict_to_hosts_none(inventory_manager):
    inventory_manager.restrict_to_hosts(None)
    assert inventory_manager._restriction is None

def test_restrict_to_hosts_single_host(inventory_manager):
    host = Host(name='host1')
    inventory_manager.restrict_to_hosts(host)
    assert inventory_manager._restriction == {to_text(host.name)}

def test_restrict_to_hosts_multiple_hosts(inventory_manager):
    host1 = Host(name='host1')
    host2 = Host(name='host2')
    inventory_manager.restrict_to_hosts([host1, host2])
    assert inventory_manager._restriction == {to_text(host1.name), to_text(host2.name)}
