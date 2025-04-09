# file lib/ansible/cli/console.py:302-320
# lines [311, 312, 313, 314, 315, 316, 318, 320]
# branches ['311->312', '311->313', '313->314', '313->315', '315->316', '315->318']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the display module to prevent actual prints during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display.display')

# Create a fixture for the ConsoleCLI instance
@pytest.fixture
def console_cli(mock_display):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    cli = ConsoleCLI(['console'])
    cli.inventory = inventory
    cli.display = Display()
    cli.display.display = MagicMock()
    return cli

# Test function to cover lines 311-320
def test_do_cd(console_cli):
    # Test with no argument
    console_cli.do_cd('')
    assert console_cli.cwd == '*', "The current working directory should be set to '*' when no argument is provided."

    # Test with '*' argument
    console_cli.do_cd('*')
    assert console_cli.cwd == 'all', "The current working directory should be set to 'all' when '*' is provided."

    # Test with '/' argument
    console_cli.do_cd('/')
    assert console_cli.cwd == 'all', "The current working directory should be set to 'all' when '/' is provided."

    # Test with a valid host pattern
    console_cli.inventory.add_host('testhost')
    console_cli.do_cd('testhost')
    assert console_cli.cwd == 'testhost', "The current working directory should be set to the host pattern when a valid host is provided."

    # Test with an invalid host pattern
    console_cli.do_cd('invalidhost')
    console_cli.display.display.assert_called_with("no host matched"), "Display should be called with 'no host matched' when an invalid host pattern is provided."
