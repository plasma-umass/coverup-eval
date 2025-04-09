# file lib/ansible/cli/console.py:340-346
# lines [340, 342, 343, 344, 346]
# branches ['342->343', '342->346']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    mocker.patch('cmd.Cmd.__init__', return_value=None)
    return ConsoleCLI(args=[])

def test_do_remote_user_with_arg(console_cli, mocker):
    mocker.patch.object(console_cli, 'set_prompt')
    console_cli.do_remote_user('testuser')
    assert console_cli.remote_user == 'testuser'
    console_cli.set_prompt.assert_called_once()

def test_do_remote_user_without_arg(console_cli, mocker):
    display_mock = mocker.patch.object(Display, 'display')
    console_cli.do_remote_user('')
    display_mock.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
