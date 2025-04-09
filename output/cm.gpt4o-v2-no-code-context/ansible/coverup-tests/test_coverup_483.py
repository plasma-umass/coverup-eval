# file: lib/ansible/cli/console.py:340-346
# asked: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}
# gained: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli(mocker):
    mock_args = mocker.MagicMock()
    return ConsoleCLI(mock_args)

def test_do_remote_user_with_arg(console_cli, mocker):
    mocker.patch.object(console_cli, 'set_prompt')
    console_cli.do_remote_user('testuser')
    assert console_cli.remote_user == 'testuser'
    console_cli.set_prompt.assert_called_once()

def test_do_remote_user_without_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_remote_user('')
    mock_display.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
