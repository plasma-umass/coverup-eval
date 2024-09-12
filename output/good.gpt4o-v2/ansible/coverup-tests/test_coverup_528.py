# file: lib/ansible/cli/console.py:340-346
# asked: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}
# gained: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_do_remote_user_with_arg(console_cli):
    with patch.object(console_cli, 'set_prompt') as mock_set_prompt:
        console_cli.do_remote_user('test_user')
        assert console_cli.remote_user == 'test_user'
        mock_set_prompt.assert_called_once()

def test_do_remote_user_without_arg(console_cli):
    with patch.object(Display, 'display') as mock_display:
        console_cli.do_remote_user('')
        mock_display.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
