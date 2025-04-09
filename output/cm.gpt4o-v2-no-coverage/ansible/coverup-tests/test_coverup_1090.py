# file: lib/ansible/inventory/manager.py:551-588
# asked: {"lines": [557, 559, 560, 561, 562, 565, 567, 568, 569, 570, 572, 574, 575, 576, 579, 580, 581, 582, 583, 584, 585, 588], "branches": [[560, 561], [560, 565], [561, 562], [561, 565], [565, 567], [565, 572], [568, 569], [568, 572], [569, 570], [569, 572], [572, 574], [572, 579], [575, 576], [575, 579], [579, 580], [579, 588], [582, 583], [582, 584], [584, 585], [584, 588]]}
# gained: {"lines": [557, 559, 560, 561, 562, 565, 567, 568, 569, 570, 572, 574, 575, 576, 579, 580, 581, 582, 583, 584, 585, 588], "branches": [[560, 561], [560, 565], [561, 562], [561, 565], [565, 567], [565, 572], [568, 569], [568, 572], [569, 570], [569, 572], [572, 574], [572, 579], [575, 576], [579, 580], [579, 588], [582, 583], [582, 584], [584, 585]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from ansible import constants as C

class MockInventory:
    def __init__(self, groups, hosts):
        self.groups = groups
        self.hosts = hosts

    def get_host(self, pattern):
        if pattern in C.LOCALHOST:
            return "localhost"
        return None

class MockGroup:
    def __init__(self, hosts):
        self.hosts = hosts

    def get_hosts(self):
        return self.hosts

class MockDisplay:
    def __init__(self):
        self.messages = {"debug": [], "warning": []}

    def debug(self, msg):
        self.messages["debug"].append(msg)

    def warning(self, msg):
        self.messages["warning"].append(msg)

@pytest.fixture
def mock_inventory():
    groups = {
        "group1": MockGroup(["host1", "host2"]),
        "group2": MockGroup(["host3"])
    }
    hosts = {
        "host1": "host1",
        "host2": "host2",
        "host3": "host3",
        "host4": "host4"
    }
    return MockInventory(groups, hosts)

@pytest.fixture
def mock_display(monkeypatch):
    display = MockDisplay()
    monkeypatch.setattr("ansible.inventory.manager.display", display)
    return display

@pytest.fixture
def inventory_manager(mock_inventory, monkeypatch):
    class MockLoader:
        pass

    loader = MockLoader()
    manager = InventoryManager(loader)
    manager._inventory = mock_inventory
    return manager

def test_enumerate_matches_group_pattern(inventory_manager):
    pattern = "group1"
    result = inventory_manager._enumerate_matches(pattern)
    assert result == ["host1", "host2"]

def test_enumerate_matches_host_pattern(inventory_manager):
    pattern = "host3"
    result = inventory_manager._enumerate_matches(pattern)
    assert result == ["host3"]

def test_enumerate_matches_regex_pattern(inventory_manager):
    pattern = "host[1-2]"
    result = inventory_manager._enumerate_matches(pattern)
    assert result == ["host1", "host2"]

def test_enumerate_matches_localhost_pattern(inventory_manager):
    pattern = "localhost"
    result = inventory_manager._enumerate_matches(pattern)
    assert result == ["localhost"]

def test_enumerate_matches_no_match_warning(inventory_manager, mock_display):
    pattern = "nonexistent"
    result = inventory_manager._enumerate_matches(pattern)
    assert result == []
    assert mock_display.messages["debug"] == ["Could not match supplied host pattern, ignoring: nonexistent"]
    assert mock_display.messages["warning"] == ["Could not match supplied host pattern, ignoring: nonexistent"]

def test_enumerate_matches_no_match_error(inventory_manager, mock_display, monkeypatch):
    monkeypatch.setattr(C, "HOST_PATTERN_MISMATCH", "error")
    pattern = "nonexistent"
    with pytest.raises(AnsibleError, match="Could not match supplied host pattern, ignoring: nonexistent"):
        inventory_manager._enumerate_matches(pattern)
