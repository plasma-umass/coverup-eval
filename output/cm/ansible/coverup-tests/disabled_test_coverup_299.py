# file lib/ansible/cli/console.py:384-396
# lines [384, 386, 387, 388, 389, 390, 392, 393, 394, 396]
# branches ['386->387', '386->396', '389->390', '389->392']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to capture output
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'display')

@pytest.fixture
def mock_error_display(mocker):
    return mocker.patch.object(Display, 'error')

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    return ConsoleCLI(args=[])

def test_do_timeout_with_positive_integer(console_cli, mock_display, mock_error_display):
    console_cli.do_timeout('10')
    assert console_cli.task_timeout == 10
    mock_display.assert_not_called()
    mock_error_display.assert_not_called()

def test_do_timeout_with_zero(console_cli, mock_display, mock_error_display):
    console_cli.do_timeout('0')
    assert console_cli.task_timeout == 0
    mock_display.assert_not_called()
    mock_error_display.assert_not_called()

def test_do_timeout_with_negative_integer(console_cli, mock_display, mock_error_display):
    console_cli.do_timeout('-1')
    mock_error_display.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')
    assert console_cli.task_timeout is None

def test_do_timeout_with_invalid_value(console_cli, mock_display, mock_error_display):
    console_cli.do_timeout('invalid')
    mock_error_display.assert_called_once()
    assert 'The timeout must be a valid positive integer, or 0 to disable:' in mock_error_display.call_args[0][0]
    assert console_cli.task_timeout is None

def test_do_timeout_with_no_argument(console_cli, mock_display, mock_error_display):
    console_cli.do_timeout('')
    mock_display.assert_called_once_with('Usage: timeout <seconds>')
    mock_error_display.assert_not_called()
