# file lib/ansible/plugins/become/su.py:146-161
# lines [146, 147, 151, 153, 154, 156, 157, 158, 159, 161]
# branches ['153->154', '153->156']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.become.su import BecomeModule

@pytest.fixture
def become_module():
    return BecomeModule()

def test_build_become_command(become_module, mocker):
    mocker.patch.object(become_module, 'get_option', side_effect=lambda x: {
        'become_exe': 'su',
        'become_flags': '-m',
        'become_user': 'root'
    }.get(x, ''))
    mocker.patch.object(become_module, '_build_success_command', return_value='echo success')
    mocker.patch('ansible.plugins.become.su.shlex_quote', side_effect=lambda x: f'"{x}"')

    cmd = 'whoami'
    shell = '/bin/sh'
    result = become_module.build_become_command(cmd, shell)

    assert result == 'su -m root -c "echo success"'
    assert become_module.prompt is True

def test_build_become_command_no_cmd(become_module, mocker):
    mocker.patch.object(become_module, 'get_option', return_value='')

    cmd = ''
    shell = '/bin/sh'
    result = become_module.build_become_command(cmd, shell)

    assert result == ''
    assert become_module.prompt is True
