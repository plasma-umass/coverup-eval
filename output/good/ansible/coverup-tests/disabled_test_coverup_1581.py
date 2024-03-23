# file lib/ansible/cli/console.py:275-287
# lines [277, 278, 279, 281, 282, 283, 284, 286, 287]
# branches ['277->278', '277->281', '282->283', '282->286']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')

# Test function to cover lines 277-279
def test_do_forks_no_arg(mock_display):
    console_cli = ConsoleCLI(['console'])
    console_cli.do_forks('')
    Display.display.assert_called_once_with('Usage: forks <number>')

# Test function to cover lines 281-284
def test_do_forks_invalid_arg(mock_display):
    console_cli = ConsoleCLI(['console'])
    console_cli.do_forks('0')
    Display.display.assert_called_once_with('forks must be greater than or equal to 1')

# Test function to cover lines 286-287
def test_do_forks_valid_arg(mock_display, mocker):
    console_cli = ConsoleCLI(['console'])
    mocker.patch.object(console_cli, 'set_prompt')
    console_cli.do_forks('5')
    assert console_cli.forks == 5
    console_cli.set_prompt.assert_called_once()
