# file lib/ansible/cli/inventory.py:237-244
# lines [237, 238, 240, 241, 242, 244]
# branches ['240->241', '240->244', '241->240', '241->242']

import pytest
from ansible.cli.inventory import InventoryCLI

def test_remove_internal(mocker):
    # Mock the INTERNAL_VARS to control the test environment
    mocker.patch('ansible.cli.inventory.INTERNAL_VARS', ['internal_var1', 'internal_var2'])

    # Create a sample dump dictionary with internal variables
    dump = {
        'internal_var1': 'value1',
        'internal_var2': 'value2',
        'external_var': 'value3'
    }

    # Call the _remove_internal method
    result = InventoryCLI._remove_internal(dump)

    # Assert that internal variables are removed
    assert 'internal_var1' not in result
    assert 'internal_var2' not in result
    # Assert that external variables are not removed
    assert 'external_var' in result
    assert result['external_var'] == 'value3'
