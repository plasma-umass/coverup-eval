# file lib/ansible/cli/console.py:384-396
# lines [386, 387, 388, 389, 390, 392, 393, 394, 396]
# branches ['386->387', '386->396', '389->390', '389->392']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')
    mocker.patch.object(Display, 'error')
    return Display

# Test function to cover lines 386-396
def test_do_timeout(mock_display, mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)  # Mock the __init__ of the CLI class
    console_cli = ConsoleCLI(['console'])  # Provide a non-empty list to the constructor

    # Test with a valid positive integer
    console_cli.do_timeout('10')
    assert console_cli.task_timeout == 10
    mock_display.display.assert_not_called()
    mock_display.error.assert_not_called()

    # Test with a negative integer
    console_cli.do_timeout('-1')
    mock_display.error.assert_called_with('The timeout must be greater than or equal to 1, use 0 to disable')

    # Test with a non-integer value
    console_cli.do_timeout('invalid')
    mock_display.error.assert_called_with('The timeout must be a valid positive integer, or 0 to disable: invalid literal for int() with base 10: \'invalid\'')

    # Test with no argument
    console_cli.do_timeout('')
    mock_display.display.assert_called_with('Usage: timeout <seconds>')
