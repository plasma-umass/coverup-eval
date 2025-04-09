# file lib/ansible/cli/console.py:302-320
# lines [311, 312, 313, 314, 315, 316, 318, 320]
# branches ['311->312', '311->313', '313->314', '313->315', '315->316', '315->318']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display

# Mock the display module to prevent actual prints during the test
@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch.object(display, 'display')
    return display

# Mock the InventoryManager to control the return value of get_hosts
@pytest.fixture
def mock_inventory_manager(mocker):
    inventory_manager = mocker.MagicMock(spec=InventoryManager)
    inventory_manager.get_hosts.return_value = False
    return inventory_manager

# Test function to cover lines 311-320
def test_do_cd(mock_display, mock_inventory_manager, mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)  # Mock CLI.__init__ to do nothing
    console_cli = ConsoleCLI(['console'])  # Provide a non-empty list to avoid ValueError
    console_cli.inventory = mock_inventory_manager
    console_cli.set_prompt = lambda: None  # Mock set_prompt to do nothing
    console_cli.display = mock_display  # Use the mocked display

    # Test with no argument (should set cwd to '*')
    console_cli.do_cd('')
    assert console_cli.cwd == '*'
    mock_display.display.assert_not_called()  # No display should be called

    # Test with argument '/*' (should set cwd to 'all')
    console_cli.do_cd('/*')
    assert console_cli.cwd == 'all'
    mock_display.display.assert_not_called()  # No display should be called

    # Test with an argument that does not match any hosts (should display "no host matched")
    console_cli.do_cd('nonexistent')
    assert console_cli.cwd != 'nonexistent'  # cwd should not be set to the invalid arg
    mock_display.display.assert_called_once_with("no host matched")  # Display should be called once

    # Reset mock_display for the next test
    mock_display.display.reset_mock()

    # Test with an argument that matches hosts (should set cwd to the argument)
    mock_inventory_manager.get_hosts.return_value = True  # Mock get_hosts to return True
    console_cli.do_cd('existent')
    assert console_cli.cwd == 'existent'
    mock_display.display.assert_not_called()  # No display should be called
