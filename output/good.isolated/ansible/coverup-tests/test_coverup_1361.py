# file lib/ansible/inventory/manager.py:348-363
# lines [354, 355, 356]
# branches ['351->354']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

# Assuming the InventoryManager class is part of a larger module, we'll need to mock out
# any dependencies and ensure the test is isolated.

class MockLoader:
    pass

@pytest.fixture
def inventory_manager():
    # Mock the loader as it is a required argument for InventoryManager
    loader = MockLoader()
    return InventoryManager(loader=loader)

def test_inventory_manager_match_list_invalid_pattern(inventory_manager):
    items = ['host1', 'host2', 'host3']
    invalid_pattern_str = '~['  # This pattern is invalid because it contains an unclosed character set

    # Exercise & Verify
    with pytest.raises(AnsibleError) as excinfo:
        inventory_manager._match_list(items, invalid_pattern_str)
    assert 'Invalid host list pattern' in str(excinfo.value)

    # No cleanup is necessary as we haven't modified any external state
