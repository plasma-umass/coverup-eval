# file lib/ansible/cli/inventory.py:253-258
# lines [253, 254, 255, 256, 257, 258]
# branches ['256->257', '256->258']

import pytest
from ansible.cli.inventory import InventoryCLI

# Assuming the InventoryCLI and _graph_name method are defined as provided in the context

class TestInventoryCLI:

    @staticmethod
    def test_show_vars():
        # Setup
        dump = {
            'key1': 'value1',
            'key2': 'value2',
        }
        depth = 1

        # Exercise
        result = InventoryCLI._show_vars(dump, depth)

        # Verify
        expected = [
            InventoryCLI._graph_name('{key1 = value1}', depth),
            InventoryCLI._graph_name('{key2 = value2}', depth),
        ]
        assert result == expected

        # Cleanup - nothing to clean up as the test does not affect external state
