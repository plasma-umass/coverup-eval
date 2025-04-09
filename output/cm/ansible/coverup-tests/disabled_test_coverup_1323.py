# file lib/ansible/cli/console.py:331-338
# lines [333, 334, 335, 336, 338]
# branches ['333->334', '333->338']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'v')
    mocker.patch.object(Display, 'display')

# Test function to cover lines 333-338
def test_do_become(mock_display):
    console_cli = ConsoleCLI(['console'])
    # Mock the inventory and set_prompt to prevent side effects
    console_cli.inventory = MagicMock()
    console_cli.set_prompt = MagicMock()
    # Set initial become value
    console_cli.become = None
    # Test with arg to cover lines 333-335
    console_cli.do_become('yes')
    assert console_cli.become is True
    Display.v.assert_called_once_with("become changed to True")
    Display.v.reset_mock()

    # Test without arg to cover line 338
    console_cli.do_become('')
    Display.display.assert_called_once_with("Please specify become value, e.g. `become yes`")
