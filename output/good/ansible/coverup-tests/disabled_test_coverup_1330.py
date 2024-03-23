# file lib/ansible/cli/console.py:340-346
# lines [342, 343, 344, 346]
# branches ['342->343', '342->346']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'display')

# Test function to cover lines 342-346
def test_do_remote_user(mock_display, mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)  # Mock CLI.__init__ to do nothing
    console_cli = ConsoleCLI(args=[])  # Provide an empty list for args
    console_cli.set_prompt = lambda: None  # Mock set_prompt to do nothing

    # Test with a non-empty argument to cover lines 342-344
    test_user = 'testuser'
    console_cli.do_remote_user(test_user)
    assert console_cli.remote_user == test_user, "Remote user should be set to the provided argument"

    # Test with an empty argument to cover line 346
    console_cli.do_remote_user('')
    Display.display.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
