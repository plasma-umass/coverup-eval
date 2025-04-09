# file lib/ansible/cli/inventory.py:46-51
# lines [46, 47, 49, 50]
# branches []

import pytest
from ansible.cli.inventory import InventoryCLI

def test_inventory_cli_arguments():
    # Verify that the ARGUMENTS dictionary contains the expected keys and values
    expected_arguments = {
        'host': 'The name of a host to match in the inventory, relevant when using --list',
        'group': 'The name of a group in the inventory, relevant when using --graph',
    }
    assert InventoryCLI.ARGUMENTS == expected_arguments
