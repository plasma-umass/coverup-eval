# file: lib/ansible/cli/console.py:291-300
# asked: {"lines": [293, 294, 296, 297, 298, 299, 300], "branches": [[293, 294], [293, 296]]}
# gained: {"lines": [293, 294, 296, 297, 298, 299, 300], "branches": [[293, 294], [293, 296]]}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

@pytest.fixture
def mock_display():
    with patch('ansible.cli.console.display', new_callable=MagicMock) as mock_display:
        yield mock_display

def test_do_verbosity_no_arg(console_cli, mock_display):
    console_cli.do_verbosity('')
    mock_display.display.assert_called_once_with('Usage: verbosity <number>')

def test_do_verbosity_valid_arg(console_cli, mock_display):
    console_cli.do_verbosity('3')
    assert mock_display.verbosity == 3
    mock_display.v.assert_called_once_with('verbosity level set to 3')

def test_do_verbosity_invalid_arg(console_cli, mock_display):
    console_cli.do_verbosity('invalid')
    mock_display.error.assert_called_once_with('The verbosity must be a valid integer: invalid literal for int() with base 10: \'invalid\'')

def test_do_verbosity_type_error(console_cli, mock_display):
    with patch('ansible.cli.console.int', side_effect=TypeError('type error')):
        console_cli.do_verbosity('3')
        mock_display.error.assert_called_once_with('The verbosity must be a valid integer: type error')
