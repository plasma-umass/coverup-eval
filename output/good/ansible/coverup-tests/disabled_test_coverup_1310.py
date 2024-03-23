# file lib/ansible/cli/console.py:348-355
# lines [350, 351, 353, 354, 355]
# branches ['350->351', '350->353']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')
    mocker.patch.object(Display, 'v')
    return Display

# Test function to cover lines 350-355
def test_do_become_user(mock_display, mocker):
    mocker.patch('ansible.cli.console.ConsoleCLI.set_prompt')  # Mock set_prompt to prevent side effects
    console_cli = ConsoleCLI(['ansible-console'])  # Provide a non-empty list to ConsoleCLI
    console_cli.become_user = 'initial_user'

    # Test with a non-empty arg to cover line 351
    console_cli.do_become_user('new_user')
    assert console_cli.become_user == 'new_user'
    mock_display.display.assert_not_called()
    mock_display.v.assert_not_called()

    # Reset mock calls
    mock_display.display.reset_mock()
    mock_display.v.reset_mock()

    # Test with an empty arg to cover lines 353-355
    console_cli.do_become_user('')
    mock_display.display.assert_called_once_with("Please specify a user, e.g. `become_user jenkins`")
    mock_display.v.assert_called_once_with("Current user is new_user")
