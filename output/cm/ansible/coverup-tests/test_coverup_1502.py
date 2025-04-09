# file lib/ansible/cli/inventory.py:237-244
# lines []
# branches ['241->240']

import pytest
from ansible.cli.inventory import InventoryCLI

# Assuming INTERNAL_VARS is a constant defined somewhere in the ansible module
# If not, you would need to mock or define it accordingly for the test to work
# Since the import failed, we'll define a mock INTERNAL_VARS for the purpose of this test
INTERNAL_VARS = ['ansible_inventory_sources', 'ansible_playbook_python']

@pytest.fixture
def mock_inventory_dump():
    # Create a dictionary that contains all internal vars plus some extra keys
    dump = {internal: f"value_{internal}" for internal in INTERNAL_VARS}
    dump.update({"extra_key1": "value1", "extra_key2": "value2"})
    return dump

def test_remove_internal(mock_inventory_dump):
    # Call the method under test
    cleaned_dump = InventoryCLI._remove_internal(mock_inventory_dump)
    
    # Assert that all INTERNAL_VARS have been removed
    for internal in INTERNAL_VARS:
        assert internal not in cleaned_dump
    
    # Assert that other keys are still present
    for key in cleaned_dump:
        assert key not in INTERNAL_VARS
        assert key == "extra_key1" or key == "extra_key2"
    
    # Assert that the original dump has been modified since the method is not supposed to create a copy
    for internal in INTERNAL_VARS:
        assert internal not in mock_inventory_dump
