# file lib/ansible/cli/console.py:357-364
# lines [359, 360, 361, 363, 364]
# branches ['359->360', '359->363']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')
    mocker.patch.object(Display, 'v')

# Test function to cover lines 359-361
def test_do_become_method_with_arg(mock_display):
    console_cli = ConsoleCLI(['ansible-console'])
    test_become_method = 'sudo'
    console_cli.do_become_method(test_become_method)
    assert console_cli.become_method == test_become_method
    Display.display.assert_not_called()
    Display.v.assert_called_once_with("become_method changed to %s" % test_become_method)

# Test function to cover lines 363-364
def test_do_become_method_without_arg(mock_display):
    console_cli = ConsoleCLI(['ansible-console'])
    console_cli.become_method = 'none'  # Set an initial become_method
    console_cli.do_become_method('')
    Display.display.assert_called_once_with("Please specify a become_method, e.g. `become_method su`")
    Display.v.assert_called_once_with("Current become_method is %s" % console_cli.become_method)
