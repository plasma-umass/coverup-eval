# file: lib/ansible/inventory/host.py:153-159
# asked: {"lines": [153, 154, 155, 156, 157, 159], "branches": []}
# gained: {"lines": [153, 154, 155, 156, 157, 159], "branches": []}

import pytest
from ansible.inventory.host import Host

class MockGroup:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def host():
    return Host(name="test.example.com")

@pytest.fixture
def mock_groups():
    return [MockGroup(name="group1"), MockGroup(name="group2"), MockGroup(name="all")]

def test_get_magic_vars(monkeypatch, host, mock_groups):
    def mock_get_groups():
        return mock_groups

    monkeypatch.setattr(host, "get_groups", mock_get_groups)
    
    magic_vars = host.get_magic_vars()
    
    assert magic_vars['inventory_hostname'] == "test.example.com"
    assert magic_vars['inventory_hostname_short'] == "test"
    assert magic_vars['group_names'] == ["group1", "group2"]
