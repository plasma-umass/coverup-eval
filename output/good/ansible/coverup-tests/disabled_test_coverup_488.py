# file lib/ansible/cli/console.py:331-338
# lines [331, 333, 334, 335, 336, 338]
# branches ['333->334', '333->338']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'v')
    mocker.patch.object(Display, 'display')
    return Display

# Test function to cover the do_become method with an argument
def test_do_become_with_arg(mock_display):
    with patch('ansible.cli.console.CLI'):
        console_cli = ConsoleCLI(['console'])
        console_cli.set_prompt = MagicMock()
        arg = 'yes'
        console_cli.do_become(arg)
        mock_display.v.assert_called_once_with("become changed to True")
        console_cli.set_prompt.assert_called_once()

# Test function to cover the do_become method without an argument
def test_do_become_without_arg(mock_display):
    with patch('ansible.cli.console.CLI'):
        console_cli = ConsoleCLI(['console'])
        console_cli.do_become('')
        mock_display.display.assert_called_once_with("Please specify become value, e.g. `become yes`")
