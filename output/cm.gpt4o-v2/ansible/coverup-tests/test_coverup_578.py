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

def test_get_magic_vars(host, mocker):
    mock_groups = [MockGroup("group1"), MockGroup("group2"), MockGroup("all")]
    mocker.patch.object(host, 'get_groups', return_value=mock_groups)
    
    magic_vars = host.get_magic_vars()
    
    assert magic_vars['inventory_hostname'] == "test.example.com"
    assert magic_vars['inventory_hostname_short'] == "test"
    assert magic_vars['group_names'] == ["group1", "group2"]
