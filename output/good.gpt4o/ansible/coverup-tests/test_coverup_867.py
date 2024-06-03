# file lib/ansible/plugins/inventory/ini.py:138-139
# lines [138, 139]
# branches []

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._filename = 'test.ini'
    module.lineno = 42
    return module

def test_raise_error(inventory_module):
    with pytest.raises(AnsibleError) as excinfo:
        inventory_module._raise_error("Test error message")
    assert str(excinfo.value) == "test.ini:42: Test error message"
