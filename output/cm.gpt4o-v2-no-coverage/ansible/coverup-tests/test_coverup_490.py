# file: lib/ansible/inventory/manager.py:605-615
# asked: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}
# gained: {"lines": [605, 611, 612, 613, 614, 615], "branches": [[611, 612], [611, 613], [613, 614], [613, 615]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.module_utils._text import to_text

class MockHost:
    def __init__(self, name):
        self.name = name

class MockLoader:
    pass

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=MockLoader())

def test_restrict_to_hosts_none(inventory_manager):
    inventory_manager.restrict_to_hosts(None)
    assert inventory_manager._restriction is None

def test_restrict_to_hosts_single_host(inventory_manager):
    host = MockHost("host1")
    inventory_manager.restrict_to_hosts(host)
    assert inventory_manager._restriction == {to_text("host1")}

def test_restrict_to_hosts_multiple_hosts(inventory_manager):
    hosts = [MockHost("host1"), MockHost("host2")]
    inventory_manager.restrict_to_hosts(hosts)
    assert inventory_manager._restriction == {to_text("host1"), to_text("host2")}

def test_restrict_to_hosts_non_list(inventory_manager):
    host = MockHost("host1")
    inventory_manager.restrict_to_hosts(host)
    assert inventory_manager._restriction == {to_text("host1")}
