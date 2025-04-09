# file lib/ansible/cli/inventory.py:253-258
# lines [253, 254, 255, 256, 257, 258]
# branches ['256->257', '256->258']

import pytest
from ansible.cli.inventory import InventoryCLI

def test_inventorycli_show_vars(mocker):
    # Mock the _graph_name method to avoid any side effects
    mocker.patch.object(InventoryCLI, '_graph_name', side_effect=lambda x, y: x)

    # Define a sample input dictionary
    sample_dump = {'var1': 'value1', 'var2': 'value2'}
    depth = 1

    # Call the method
    result = InventoryCLI._show_vars(sample_dump, depth)

    # Verify the result
    expected_result = ['{var1 = value1}', '{var2 = value2}']
    assert result == expected_result
