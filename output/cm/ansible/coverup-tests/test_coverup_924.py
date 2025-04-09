# file lib/ansible/plugins/inventory/ini.py:138-139
# lines [138, 139]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.inventory.ini import InventoryModule

def test_inventory_module_raise_error(mocker):
    # Mocking the BaseFileInventoryPlugin to avoid side effects
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin')

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Set the filename and lineno attributes
    inventory_module._filename = 'test.ini'
    inventory_module.lineno = 42

    # Define the error message
    error_message = "Test error message"

    # Assert that the correct error is raised with the correct message
    with pytest.raises(AnsibleError) as exc_info:
        inventory_module._raise_error(error_message)

    # Verify the exception message
    assert str(exc_info.value) == "test.ini:42: Test error message"
