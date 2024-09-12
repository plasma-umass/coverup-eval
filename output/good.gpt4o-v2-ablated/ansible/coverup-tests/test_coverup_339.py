# file: lib/ansible/plugins/inventory/ini.py:138-139
# asked: {"lines": [138, 139], "branches": []}
# gained: {"lines": [138, 139], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.inventory.ini import InventoryModule

class MockBaseFileInventoryPlugin:
    def __init__(self, filename, lineno):
        self._filename = filename
        self.lineno = lineno

class TestInventoryModule:
    @pytest.fixture
    def inventory_module(self):
        class TestInventoryModule(MockBaseFileInventoryPlugin, InventoryModule):
            pass
        return TestInventoryModule("testfile.ini", 42)

    def test_raise_error(self, inventory_module):
        with pytest.raises(AnsibleError) as excinfo:
            inventory_module._raise_error("Test error message")
        assert str(excinfo.value) == "testfile.ini:42: Test error message"
