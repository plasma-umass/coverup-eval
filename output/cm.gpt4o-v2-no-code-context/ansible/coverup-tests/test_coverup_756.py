# file: lib/ansible/plugins/inventory/ini.py:138-139
# asked: {"lines": [138, 139], "branches": []}
# gained: {"lines": [138, 139], "branches": []}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError

@pytest.fixture
def inventory_module():
    class MockInventoryModule(InventoryModule):
        def __init__(self):
            self._filename = "testfile.ini"
            self.lineno = 42

    return MockInventoryModule()

def test_raise_error(inventory_module):
    with pytest.raises(AnsibleError) as excinfo:
        inventory_module._raise_error("Test error message")
    assert str(excinfo.value) == "testfile.ini:42: Test error message"
