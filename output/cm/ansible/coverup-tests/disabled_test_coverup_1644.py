# file lib/ansible/cli/console.py:340-346
# lines [342, 343, 344, 346]
# branches ['342->343', '342->346']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'display')

# Test function to cover lines 342-346
def test_do_remote_user(mock_display, mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    console_cli = ConsoleCLI([])
    console_cli.set_prompt = lambda: None  # Mock set_prompt to prevent side effects

    # Set a remote user and check if it's set correctly
    test_user = 'testuser'
    console_cli.do_remote_user(test_user)
    assert console_cli.remote_user == test_user

    # Call without argument to trigger the else branch
    console_cli.do_remote_user('')
    mock_display.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
