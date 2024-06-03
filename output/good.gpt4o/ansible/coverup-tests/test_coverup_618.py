# file lib/ansible/plugins/inventory/ini.py:86-94
# lines [86, 87, 91, 92, 93]
# branches []

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

def test_inventory_module_initialization():
    # Test the initialization of the InventoryModule class
    inventory_module = InventoryModule()
    
    # Verify that the NAME attribute is set correctly
    assert inventory_module.NAME == 'ini'
    
    # Verify that the _COMMENT_MARKERS attribute is set correctly
    assert inventory_module._COMMENT_MARKERS == frozenset((u';', u'#'))
    
    # Verify that the b_COMMENT_MARKERS attribute is set correctly
    assert inventory_module.b_COMMENT_MARKERS == frozenset((b';', b'#'))

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects on other tests
    yield
    mocker.stopall()
