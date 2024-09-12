# file: lib/ansible/plugins/shell/powershell.py:185-244
# asked: {"lines": [186, 189, 190, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 206, 207, 208, 243, 244], "branches": [[189, 190], [189, 194], [196, 197], [196, 202], [197, 199], [197, 200], [202, 203], [202, 204], [204, 206], [204, 208]]}
# gained: {"lines": [186, 189, 190, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 206, 207, 208, 243, 244], "branches": [[189, 190], [189, 194], [196, 197], [196, 202], [197, 199], [202, 203], [202, 204], [204, 206]]}

import pytest
import pkgutil
import shlex
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_build_module_command_pipelining_bypass(shell_module, monkeypatch):
    mock_bootstrap_wrapper = b"bootstrap script content"
    monkeypatch.setattr(pkgutil, "get_data", lambda *args: mock_bootstrap_wrapper)
    
    result = shell_module.build_module_command(env_string="", shebang="", cmd="")
    
    assert result == shell_module._encode_script(script=mock_bootstrap_wrapper, strict_mode=False, preserve_rc=False)

def test_build_module_command_non_pipelining_with_powershell_shebang(shell_module, monkeypatch):
    mock_bootstrap_wrapper = b"bootstrap script content"
    monkeypatch.setattr(pkgutil, "get_data", lambda *args: mock_bootstrap_wrapper)
    monkeypatch.setattr(shell_module, "_unquote", lambda x: x)
    
    cmd = "test_command"
    shebang = "#!powershell"
    result = shell_module.build_module_command(env_string="", shebang=shebang, cmd=cmd)
    
    expected_cmd = "type \"test_command.ps1\" | " + shell_module._encode_script(script=mock_bootstrap_wrapper, strict_mode=False, preserve_rc=False)
    assert result == expected_cmd

def test_build_module_command_non_pipelining_with_other_shebang(shell_module, monkeypatch):
    mock_bootstrap_wrapper = b"bootstrap script content"
    monkeypatch.setattr(pkgutil, "get_data", lambda *args: mock_bootstrap_wrapper)
    
    cmd = "test_command"
    shebang = "#!/bin/bash"
    result = shell_module.build_module_command(env_string="", shebang=shebang, cmd=cmd)
    
    expected_script = '''
                        Try
                        {
                            
                            /bin/bash test_command
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
                    '''.strip()
    assert shell_module._encode_script(expected_script, preserve_rc=False) == result

def test_build_module_command_non_pipelining_without_shebang(shell_module, monkeypatch):
    mock_bootstrap_wrapper = b"bootstrap script content"
    monkeypatch.setattr(pkgutil, "get_data", lambda *args: mock_bootstrap_wrapper)
    monkeypatch.setattr(shell_module, "_unquote", lambda x: x)
    
    cmd = "test_command"
    arg_path = "arg_path"
    result = shell_module.build_module_command(env_string="", shebang=None, cmd=cmd, arg_path=arg_path)
    
    expected_script = '''
                        Try
                        {
                            
                            test_command arg_path
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
                    '''.strip()
    assert shell_module._encode_script(expected_script, preserve_rc=False) == result
