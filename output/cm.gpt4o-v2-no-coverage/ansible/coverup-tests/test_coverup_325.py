# file: lib/ansible/cli/console.py:384-396
# asked: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}
# gained: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}

import pytest
from unittest.mock import Mock, patch
from ansible.cli.console import ConsoleCLI
from ansible.module_utils._text import to_text

class TestConsoleCLI:
    
    @pytest.fixture
    def console_cli(self):
        return ConsoleCLI(args=['test'])

    @patch('ansible.cli.console.display')
    def test_do_timeout_with_valid_arg(self, mock_display, console_cli):
        console_cli.do_timeout('10')
        assert console_cli.task_timeout == 10
        mock_display.error.assert_not_called()
        mock_display.display.assert_not_called()

    @patch('ansible.cli.console.display')
    def test_do_timeout_with_negative_arg(self, mock_display, console_cli):
        console_cli.do_timeout('-1')
        mock_display.error.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')
        mock_display.display.assert_not_called()

    @patch('ansible.cli.console.display')
    def test_do_timeout_with_invalid_arg(self, mock_display, console_cli):
        console_cli.do_timeout('invalid')
        mock_display.error.assert_called_once_with('The timeout must be a valid positive integer, or 0 to disable: %s' % to_text(ValueError('invalid literal for int() with base 10: \'invalid\'')))
        mock_display.display.assert_not_called()

    @patch('ansible.cli.console.display')
    def test_do_timeout_with_no_arg(self, mock_display, console_cli):
        console_cli.do_timeout('')
        mock_display.display.assert_called_once_with('Usage: timeout <seconds>')
        mock_display.error.assert_not_called()
