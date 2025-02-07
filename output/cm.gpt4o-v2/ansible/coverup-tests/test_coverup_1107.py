# file: lib/ansible/plugins/shell/powershell.py:185-244
# asked: {"lines": [186, 189, 190, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 206, 207, 208, 243, 244], "branches": [[189, 190], [189, 194], [196, 197], [196, 202], [197, 199], [197, 200], [202, 203], [202, 204], [204, 206], [204, 208]]}
# gained: {"lines": [186, 189, 190, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 206, 207, 208, 243, 244], "branches": [[189, 190], [189, 194], [196, 197], [196, 202], [197, 199], [202, 203], [202, 204], [204, 206]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_build_module_command_empty_cmd(shell_module):
    with patch('pkgutil.get_data', return_value=b'bootstrap script') as mock_get_data:
        result = shell_module.build_module_command(env_string='', shebang=None, cmd='')
        assert result == shell_module._encode_script(script=b'bootstrap script', strict_mode=False, preserve_rc=False)
        mock_get_data.assert_called_once_with("ansible.executor.powershell", "bootstrap_wrapper.ps1")

def test_build_module_command_powershell_shebang(shell_module):
    with patch('pkgutil.get_data', return_value=b'bootstrap script') as mock_get_data, \
         patch.object(ShellModule, '_unquote', return_value='module') as mock_unquote, \
         patch.object(ShellModule, '_encode_script', return_value='encoded script') as mock_encode_script:
        result = shell_module.build_module_command(env_string='', shebang='#!powershell', cmd='module')
        assert result == 'type "module.ps1" | encoded script'
        mock_get_data.assert_called_once_with("ansible.executor.powershell", "bootstrap_wrapper.ps1")
        mock_unquote.assert_called_with('module')
        mock_encode_script.assert_called_once_with(script=b'bootstrap script', strict_mode=False, preserve_rc=False)

def test_build_module_command_other_shebang(shell_module):
    with patch.object(ShellModule, '_encode_script', return_value='encoded script') as mock_encode_script:
        result = shell_module.build_module_command(env_string='', shebang='#!/bin/bash', cmd='module')
        assert result == 'encoded script'
        mock_encode_script.assert_called_once()

def test_build_module_command_no_shebang(shell_module):
    with patch.object(ShellModule, '_unquote', return_value='module') as mock_unquote, \
         patch.object(ShellModule, '_encode_script', return_value='encoded script') as mock_encode_script:
        result = shell_module.build_module_command(env_string='', shebang=None, cmd='module', arg_path='arg_path')
        assert result == 'encoded script'
        mock_unquote.assert_called_with('module')
        mock_encode_script.assert_called_once()

def test_build_module_command_script(shell_module):
    with patch.object(ShellModule, '_encode_script', return_value='encoded script') as mock_encode_script:
        result = shell_module.build_module_command(env_string='env', shebang=None, cmd='module', arg_path='arg_path')
        expected_script = '''
            Try
            {
                env
                module arg_path
            }
            Catch
            {
                $_obj = @{ failed = $true }
                If ($_.Exception.GetType)
                {
                    $_obj.Add('msg', $_.Exception.Message)
                }
                Else
                {
                    $_obj.Add('msg', $_.ToString())
                }
                If ($_.InvocationInfo.PositionMessage)
                {
                    $_obj.Add('exception', $_.InvocationInfo.PositionMessage)
                }
                ElseIf ($_.ScriptStackTrace)
                {
                    $_obj.Add('exception', $_.ScriptStackTrace)
                }
                Try
                {
                    $_obj.Add('error_record', ($_ | ConvertTo-Json | ConvertFrom-Json))
                }
                Catch
                {
                }
                Echo $_obj | ConvertTo-Json -Compress -Depth 99
                Exit 1
            }
        '''
        assert result == 'encoded script'
        mock_encode_script.assert_called_once_with(expected_script, preserve_rc=False)
