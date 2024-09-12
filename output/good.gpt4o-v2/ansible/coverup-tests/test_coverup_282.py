# file: lib/ansible/cli/console.py:384-396
# asked: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}
# gained: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

def test_do_timeout_with_valid_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_timeout('10')
        assert console_cli.task_timeout == 10
        mock_display.error.assert_not_called()
        mock_display.display.assert_not_called()

def test_do_timeout_with_negative_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_timeout('-1')
        mock_display.error.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')
        mock_display.display.assert_not_called()

def test_do_timeout_with_invalid_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_timeout('invalid')
        mock_display.error.assert_called_once_with('The timeout must be a valid positive integer, or 0 to disable: invalid literal for int() with base 10: \'invalid\'')
        mock_display.display.assert_not_called()

def test_do_timeout_with_no_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_timeout('')
        mock_display.display.assert_called_once_with('Usage: timeout <seconds>')
        mock_display.error.assert_not_called()
