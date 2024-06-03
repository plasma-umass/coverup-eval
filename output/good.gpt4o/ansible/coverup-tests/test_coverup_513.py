# file lib/ansible/cli/playbook.py:213-217
# lines [213, 214, 215, 216, 217]
# branches ['215->exit', '215->216']

import pytest
from unittest.mock import MagicMock

# Assuming the PlaybookCLI class is defined in ansible.cli.playbook module
from ansible.cli.playbook import PlaybookCLI

def test_playbookcli_flush_cache(mocker):
    # Mock the inventory and variable_manager
    inventory = MagicMock()
    variable_manager = MagicMock()

    # Create a mock host with a get_name method
    mock_host = MagicMock()
    mock_host.get_name.return_value = 'test_host'
    inventory.list_hosts.return_value = [mock_host]

    # Call the _flush_cache method
    PlaybookCLI._flush_cache(inventory, variable_manager)

    # Assert that list_hosts was called on the inventory
    inventory.list_hosts.assert_called_once()

    # Assert that get_name was called on the host
    mock_host.get_name.assert_called_once()

    # Assert that clear_facts was called on the variable_manager with the correct hostname
    variable_manager.clear_facts.assert_called_once_with('test_host')
