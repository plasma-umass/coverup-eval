# file lib/ansible/cli/console.py:366-373
# lines [366, 368, 369, 370, 372, 373]
# branches ['368->369', '368->372']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')
    mocker.patch.object(Display, 'v')
    return Display()

# Test function to cover both branches of the do_check method
def test_do_check(mock_display, mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)  # Mock CLI.__init__ to not require args
    mocker.patch('ansible.cli.console.cmd.Cmd.__init__', return_value=None)  # Mock cmd.Cmd.__init__ to not require args
    console_cli = ConsoleCLI(mock_display)

    # Set initial check_mode to False
    console_cli.check_mode = False

    # Test with no argument
    console_cli.do_check('')
    mock_display.display.assert_called_with("Please specify check mode value, e.g. `check yes`")
    mock_display.v.assert_called_with("check mode is currently False.")

    # Reset mock
    mock_display.display.reset_mock()
    mock_display.v.reset_mock()

    # Test with argument 'yes'
    console_cli.do_check('yes')
    assert console_cli.check_mode is True
    mock_display.display.assert_called_with("check mode changed to True")

    # Reset mock
    mock_display.display.reset_mock()
    mock_display.v.reset_mock()

    # Test with argument 'no'
    console_cli.do_check('no')
    assert console_cli.check_mode is False
    mock_display.display.assert_called_with("check mode changed to False")
