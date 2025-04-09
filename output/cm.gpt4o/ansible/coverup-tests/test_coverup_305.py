# file lib/ansible/cli/console.py:384-396
# lines [384, 386, 387, 388, 389, 390, 392, 393, 394, 396]
# branches ['386->387', '386->396', '389->390', '389->392']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    mocker.patch('cmd.Cmd.__init__', return_value=None)
    cli = ConsoleCLI(args=[])
    cli.task_timeout = None
    return cli

def test_do_timeout_valid(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    console_cli.do_timeout('10')
    assert console_cli.task_timeout == 10
    mock_display.assert_not_called()

def test_do_timeout_zero(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    console_cli.do_timeout('0')
    assert console_cli.task_timeout == 0
    mock_display.assert_not_called()

def test_do_timeout_negative(console_cli, mocker):
    mock_error = mocker.patch('ansible.utils.display.Display.error')
    console_cli.do_timeout('-1')
    mock_error.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')

def test_do_timeout_invalid_string(console_cli, mocker):
    mock_error = mocker.patch('ansible.utils.display.Display.error')
    console_cli.do_timeout('invalid')
    mock_error.assert_called_once_with('The timeout must be a valid positive integer, or 0 to disable: invalid literal for int() with base 10: \'invalid\'')

def test_do_timeout_no_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    console_cli.do_timeout('')
    mock_display.assert_called_once_with('Usage: timeout <seconds>')
