# file: lib/ansible/plugins/become/su.py:146-161
# asked: {"lines": [147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}
# gained: {"lines": [147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}

import pytest
from ansible.plugins.become import BecomeBase
from ansible.plugins.become.su import BecomeModule
from unittest.mock import patch, MagicMock

@pytest.fixture
def become_module():
    return BecomeModule()

def test_build_become_command_no_cmd(become_module):
    cmd = ""
    shell = "/bin/sh"
    
    result = become_module.build_become_command(cmd, shell)
    
    assert result == cmd
    assert become_module.prompt is True

@patch.object(BecomeModule, 'get_option', side_effect=lambda x: {'become_exe': 'su', 'become_flags': '-l', 'become_user': 'root'}.get(x, ''))
@patch.object(BecomeModule, '_build_success_command', return_value='echo success')
def test_build_become_command_with_cmd(mock_build_success_command, mock_get_option, become_module):
    cmd = "whoami"
    shell = "/bin/sh"
    
    result = become_module.build_become_command(cmd, shell)
    
    assert result == "su -l root -c 'echo success'"
    assert become_module.prompt is True
    mock_get_option.assert_any_call('become_exe')
    mock_get_option.assert_any_call('become_flags')
    mock_get_option.assert_any_call('become_user')
    mock_build_success_command.assert_called_once_with(cmd, shell)
