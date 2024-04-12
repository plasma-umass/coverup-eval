# file lib/ansible/plugins/shell/powershell.py:185-244
# lines [185, 186, 189, 190, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 206, 207, 208, 243, 244]
# branches ['189->190', '189->194', '196->197', '196->202', '197->199', '197->200', '202->203', '202->204', '204->206', '204->208']

import pytest
import pkgutil
from ansible.plugins.shell.powershell import ShellModule
from ansible.module_utils._text import to_text
from unittest.mock import patch, MagicMock

@pytest.fixture
def powershell_shell_module():
    return ShellModule()

@pytest.fixture
def bootstrap_wrapper_mock():
    with patch('pkgutil.get_data', return_value=b'bootstrap content') as mock:
        yield mock

def test_build_module_command_with_shebang_powershell(powershell_shell_module, bootstrap_wrapper_mock):
    env_string = ''
    shebang = '#!powershell'
    cmd = 'Test-Command'
    arg_path = None

    with patch('shlex.split', return_value=['Test-Command']), \
         patch('ansible.plugins.shell.powershell.ShellModule._unquote', return_value='Test-Command'), \
         patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value='encoded_script') as encode_script_mock:
        result = powershell_shell_module.build_module_command(env_string, shebang, cmd, arg_path)

    encode_script_mock.assert_called_once()
    assert result == 'type "Test-Command.ps1" | encoded_script'

def test_build_module_command_with_shebang_other(powershell_shell_module, bootstrap_wrapper_mock):
    env_string = ''
    shebang = '#!/usr/bin/python'
    cmd = 'Test-Command'
    arg_path = None

    with patch('shlex.split', return_value=['Test-Command']), \
         patch('ansible.plugins.shell.powershell.ShellModule._unquote', return_value='Test-Command'), \
         patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value='encoded_script') as encode_script_mock:
        result = powershell_shell_module.build_module_command(env_string, shebang, cmd, arg_path)

    encode_script_mock.assert_called_once()
    assert result.startswith('encoded_script')

def test_build_module_command_without_shebang(powershell_shell_module, bootstrap_wrapper_mock):
    env_string = ''
    shebang = None
    cmd = 'Test-Command'
    arg_path = 'arg_path'

    with patch('shlex.split', return_value=['Test-Command']), \
         patch('ansible.plugins.shell.powershell.ShellModule._unquote', return_value='Test-Command'), \
         patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value='encoded_script') as encode_script_mock:
        result = powershell_shell_module.build_module_command(env_string, shebang, cmd, arg_path)

    encode_script_mock.assert_called_once()
    assert result.startswith('encoded_script')
