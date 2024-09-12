# file: lib/ansible/plugins/inventory/ini.py:138-139
# asked: {"lines": [139], "branches": []}
# gained: {"lines": [139], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.inventory.ini import InventoryModule

def test_raise_error():
    inventory_module = InventoryModule()
    inventory_module._filename = "test_file.ini"
    inventory_module.lineno = 42
    with pytest.raises(AnsibleError) as excinfo:
        inventory_module._raise_error("Test error message")
    assert str(excinfo.value) == "test_file.ini:42: Test error message"
