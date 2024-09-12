# file: lib/ansible/plugins/become/su.py:146-161
# asked: {"lines": [146, 147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}
# gained: {"lines": [146, 147, 151, 153, 154, 156, 157, 158, 159, 161], "branches": [[153, 154], [153, 156]]}

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

def test_build_become_command_with_cmd(become_module, monkeypatch):
    cmd = "echo hello"
    shell = "/bin/sh"
    
    monkeypatch.setattr(become_module, 'get_option', lambda x: {
        'become_exe': 'su',
        'become_flags': '-m',
        'become_user': 'root'
    }.get(x, ''))
    
    mock_build_success_command = MagicMock(return_value=cmd)
    monkeypatch.setattr(become_module, '_build_success_command', mock_build_success_command)
    
    result = become_module.build_become_command(cmd, shell)
    
    assert result == "su -m root -c 'echo hello'"
    assert become_module.prompt is True
    mock_build_success_command.assert_called_once_with(cmd, shell)
