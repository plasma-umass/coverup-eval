# file: lib/ansible/cli/console.py:384-396
# asked: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}
# gained: {"lines": [384, 386, 387, 388, 389, 390, 392, 393, 394, 396], "branches": [[386, 387], [386, 396], [389, 390], [389, 392]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_do_timeout_with_valid_arg(monkeypatch, console_cli):
    display = mock.Mock(wraps=Display())
    monkeypatch.setattr('ansible.cli.console.display', display)
    
    console_cli.do_timeout('10')
    
    assert console_cli.task_timeout == 10
    display.error.assert_not_called()
    display.display.assert_not_called()

def test_do_timeout_with_negative_arg(monkeypatch, console_cli):
    display = mock.Mock(wraps=Display())
    monkeypatch.setattr('ansible.cli.console.display', display)
    
    console_cli.do_timeout('-1')
    
    display.error.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')
    display.display.assert_not_called()

def test_do_timeout_with_invalid_arg(monkeypatch, console_cli):
    display = mock.Mock(wraps=Display())
    monkeypatch.setattr('ansible.cli.console.display', display)
    
    console_cli.do_timeout('invalid')
    
    display.error.assert_called_once_with('The timeout must be a valid positive integer, or 0 to disable: invalid literal for int() with base 10: \'invalid\'')
    display.display.assert_not_called()

def test_do_timeout_with_no_arg(monkeypatch, console_cli):
    display = mock.Mock(wraps=Display())
    monkeypatch.setattr('ansible.cli.console.display', display)
    
    console_cli.do_timeout('')
    
    display.display.assert_called_once_with('Usage: timeout <seconds>')
    display.error.assert_not_called()
