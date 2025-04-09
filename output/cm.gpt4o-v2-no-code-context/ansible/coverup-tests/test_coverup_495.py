# file: lib/ansible/inventory/manager.py:590-599
# asked: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}
# gained: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}

import pytest
from ansible.inventory.manager import InventoryManager
import ansible.constants as C

class MockInventoryManager(InventoryManager):
    def __init__(self):
        pass

    def get_hosts(self, pattern):
        if pattern == "all":
            return ["host1", "host2"]
        elif pattern == "none":
            return []
        return []

@pytest.fixture
def inventory_manager():
    return MockInventoryManager()

def test_list_hosts_all(inventory_manager):
    result = inventory_manager.list_hosts("all")
    assert result == ["host1", "host2"]

def test_list_hosts_none(inventory_manager, monkeypatch):
    monkeypatch.setattr(C, "LOCALHOST", ["none"])
    result = inventory_manager.list_hosts("none")
    assert result == ["none"]

def test_list_hosts_empty_pattern(inventory_manager, monkeypatch):
    monkeypatch.setattr(C, "LOCALHOST", [""])
    result = inventory_manager.list_hosts("")
    assert result == [""]
