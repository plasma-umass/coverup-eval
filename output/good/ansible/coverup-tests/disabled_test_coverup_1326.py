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

# Test function to cover lines 359-364
def test_do_become_method(mock_display):
    # Provide a non-empty list for args to avoid ValueError
    console_cli = ConsoleCLI(['ansible-console'])

    # Set an initial become_method
    console_cli.become_method = 'sudo'

    # Test with a non-empty arg to cover lines 359-361
    test_become_method = 'su'
    console_cli.do_become_method(test_become_method)
    assert console_cli.become_method == test_become_method
    Display.v.assert_called_with(f"become_method changed to {test_become_method}")

    # Reset mock calls
    Display.display.reset_mock()
    Display.v.reset_mock()

    # Test with an empty arg to cover lines 363-364
    console_cli.do_become_method('')
    Display.display.assert_called_with("Please specify a become_method, e.g. `become_method su`")
    Display.v.assert_called_with(f"Current become_method is {test_become_method}")
