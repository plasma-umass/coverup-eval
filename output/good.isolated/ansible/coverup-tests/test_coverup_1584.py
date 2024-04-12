# file lib/ansible/cli/console.py:384-396
# lines [386, 387, 388, 389, 390, 392, 393, 394, 396]
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
def console_cli():
    # Provide a dummy argument to satisfy the non-empty list requirement
    return ConsoleCLI(['dummy_arg'])

def test_do_timeout_with_no_arg(console_cli, mock_display):
    console_cli.do_timeout('')
    mock_display.assert_called_once_with('Usage: timeout <seconds>')

def test_do_timeout_with_negative_arg(console_cli, mock_error_display):
    console_cli.do_timeout('-1')
    mock_error_display.assert_called_once_with('The timeout must be greater than or equal to 1, use 0 to disable')

def test_do_timeout_with_invalid_arg(console_cli, mock_error_display):
    console_cli.do_timeout('invalid')
    mock_error_display.assert_called_once_with('The timeout must be a valid positive integer, or 0 to disable: invalid literal for int() with base 10: \'invalid\'')

def test_do_timeout_with_valid_arg(console_cli):
    console_cli.do_timeout('10')
    assert console_cli.task_timeout == 10
