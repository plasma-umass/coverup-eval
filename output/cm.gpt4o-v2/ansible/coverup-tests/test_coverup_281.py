# file: lib/ansible/cli/console.py:275-287
# asked: {"lines": [275, 277, 278, 279, 281, 282, 283, 284, 286, 287], "branches": [[277, 278], [277, 281], [282, 283], [282, 286]]}
# gained: {"lines": [275, 277, 278, 279, 281, 282, 283, 284, 286, 287], "branches": [[277, 278], [277, 281], [282, 283], [282, 286]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_do_forks_no_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_forks('')
    mock_display.assert_called_once_with('Usage: forks <number>')

def test_do_forks_invalid_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_forks('0')
    mock_display.assert_called_once_with('forks must be greater than or equal to 1')

def test_do_forks_valid_arg(console_cli, mocker):
    mock_set_prompt = mocker.patch.object(console_cli, 'set_prompt')
    console_cli.do_forks('5')
    assert console_cli.forks == 5
    mock_set_prompt.assert_called_once()
