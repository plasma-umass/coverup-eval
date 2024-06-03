# file lib/ansible/cli/console.py:275-287
# lines [275, 277, 278, 279, 281, 282, 283, 284, 286, 287]
# branches ['277->278', '277->281', '282->283', '282->286']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.display')

def test_do_forks_no_arg(console_cli, mock_display):
    console_cli.do_forks('')
    mock_display.assert_called_once_with('Usage: forks <number>')

def test_do_forks_invalid_arg(console_cli, mock_display):
    console_cli.do_forks('0')
    mock_display.assert_called_once_with('forks must be greater than or equal to 1')

def test_do_forks_valid_arg(console_cli, mock_display):
    with mock.patch.object(console_cli, 'set_prompt') as mock_set_prompt:
        console_cli.do_forks('5')
        assert console_cli.forks == 5
        mock_set_prompt.assert_called_once()
