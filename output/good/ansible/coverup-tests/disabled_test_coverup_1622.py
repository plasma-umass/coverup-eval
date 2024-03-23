# file lib/ansible/cli/console.py:331-338
# lines [333, 334, 335, 336, 338]
# branches ['333->334', '333->338']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'v')
    mocker.patch.object(Display, 'display')

# Test function to cover lines 333-338
def test_do_become(mock_display):
    # Provide a non-empty list for args to avoid ValueError
    console_cli = ConsoleCLI(['ansible-console'])

    # Set up a mock for set_prompt method to prevent side effects
    console_cli.set_prompt = lambda: None

    # Test with a truthy value to cover lines 333-335
    console_cli.do_become('yes')
    assert console_cli.become is True
    Display.v.assert_called_with("become changed to True")

    # Reset mock
    Display.v.reset_mock()

    # Test with a falsy value to cover lines 333-335
    console_cli.do_become('no')
    assert console_cli.become is False
    Display.v.assert_called_with("become changed to False")

    # Test with an empty string to cover line 338
    console_cli.do_become('')
    Display.display.assert_called_with("Please specify become value, e.g. `become yes`")
