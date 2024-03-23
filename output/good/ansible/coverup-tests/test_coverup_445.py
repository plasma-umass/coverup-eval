# file lib/ansible/cli/inventory.py:237-244
# lines [237, 238, 240, 241, 242, 244]
# branches ['240->241', '240->244', '241->240', '241->242']

import pytest
from ansible.cli.inventory import InventoryCLI

# Assuming INTERNAL_VARS is a constant defined somewhere in the ansible module
# If not, we'll need to define it for the purpose of this test
INTERNAL_VARS = ['ansible_version', 'ansible_playbook_python']

@pytest.fixture
def inventory_cli(mocker):
    mocker.patch('ansible.cli.CLI.__init__', return_value=None)
    return InventoryCLI(args=[])

@pytest.fixture
def mock_internal_vars(mocker):
    mocker.patch('ansible.cli.inventory.INTERNAL_VARS', new=INTERNAL_VARS)

def test_remove_internal(inventory_cli, mock_internal_vars):
    # Create a dictionary that includes internal vars and other data
    test_data = {
        'ansible_version': '2.9.10',
        'ansible_playbook_python': '/usr/bin/python',
        'external_var': 'value1',
        'another_var': 'value2'
    }

    # Call the _remove_internal method
    result = inventory_cli._remove_internal(test_data.copy())

    # Assert that internal vars are removed
    for internal_var in INTERNAL_VARS:
        assert internal_var not in result

    # Assert that other data remains intact
    assert 'external_var' in result
    assert 'another_var' in result
    assert result['external_var'] == 'value1'
    assert result['another_var'] == 'value2'

    # Assert that the original dictionary is not modified
    for internal_var in INTERNAL_VARS:
        assert internal_var in test_data
    assert 'external_var' in test_data
    assert 'another_var' in test_data
