# file: lib/ansible/plugins/become/su.py:146-161
# asked: {"lines": [147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}
# gained: {"lines": [147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.become.su import BecomeModule
from ansible.module_utils.six.moves import shlex_quote

@pytest.fixture
def become_module():
    return BecomeModule()

def test_build_become_command_no_cmd(become_module):
    cmd = ""
    shell = "/bin/sh"
    result = become_module.build_become_command(cmd, shell)
    assert result == cmd
    assert become_module.prompt is True

@patch.object(BecomeModule, 'get_option')
@patch.object(BecomeModule, '_build_success_command')
def test_build_become_command_with_cmd(mock_build_success_command, mock_get_option, become_module):
    cmd = "whoami"
    shell = "/bin/sh"
    mock_get_option.side_effect = lambda x: {
        'become_exe': 'su',
        'become_flags': '-m',
        'become_user': 'root'
    }.get(x, '')
    mock_build_success_command.return_value = cmd

    result = become_module.build_become_command(cmd, shell)
    expected_command = "su -m root -c {}".format(shlex_quote(cmd))
    assert result == expected_command
    assert become_module.prompt is True
    mock_get_option.assert_any_call('become_exe')
    mock_get_option.assert_any_call('become_flags')
    mock_get_option.assert_any_call('become_user')
    mock_build_success_command.assert_called_once_with(cmd, shell)
