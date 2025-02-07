# file: lib/ansible/plugins/become/su.py:146-161
# asked: {"lines": [146, 147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}
# gained: {"lines": [146, 147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.become.su import BecomeModule
from ansible.module_utils.six.moves import shlex_quote

@pytest.fixture
def become_module():
    module = BecomeModule()
    module.get_option = MagicMock()
    module._build_success_command = MagicMock()
    return module

def test_build_become_command_no_cmd(become_module):
    cmd = ""
    shell = MagicMock()
    result = become_module.build_become_command(cmd, shell)
    assert result == cmd
    become_module.get_option.assert_not_called()
    become_module._build_success_command.assert_not_called()

def test_build_become_command_with_cmd(become_module):
    cmd = "test_command"
    shell = MagicMock()
    become_module.get_option.side_effect = lambda option: {
        'become_exe': 'su',
        'become_flags': '-m',
        'become_user': 'root'
    }.get(option, '')
    become_module._build_success_command.return_value = "success_command"
    
    result = become_module.build_become_command(cmd, shell)
    
    become_module.get_option.assert_any_call('become_exe')
    become_module.get_option.assert_any_call('become_flags')
    become_module.get_option.assert_any_call('become_user')
    become_module._build_success_command.assert_called_once_with(cmd, shell)
    
    expected_command = "su -m root -c {}".format(shlex_quote("success_command"))
    assert result == expected_command
