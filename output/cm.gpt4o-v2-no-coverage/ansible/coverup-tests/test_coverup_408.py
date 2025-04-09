# file: lib/ansible/plugins/shell/powershell.py:135-146
# asked: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}
# gained: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_expand_user_tilde(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='~')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')
    
    result = shell_module.expand_user('~')
    
    shell_module._unquote.assert_called_once_with('~')
    shell_module._encode_script.assert_called_once_with('Write-Output (Get-Location).Path')
    assert result == 'encoded_script'

def test_expand_user_tilde_backslash(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='~\\path')
    mocker.patch.object(shell_module, '_escape', return_value='\\path')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')
    
    result = shell_module.expand_user('~\\path')
    
    shell_module._unquote.assert_called_once_with('~\\path')
    shell_module._escape.assert_called_once_with('\\path')
    shell_module._encode_script.assert_called_once_with("Write-Output ((Get-Location).Path + '\\path')")
    assert result == 'encoded_script'

def test_expand_user_other(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='/other/path')
    mocker.patch.object(shell_module, '_escape', return_value='/other/path')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')
    
    result = shell_module.expand_user('/other/path')
    
    shell_module._unquote.assert_called_once_with('/other/path')
    shell_module._escape.assert_called_once_with('/other/path')
    shell_module._encode_script.assert_called_once_with("Write-Output '/other/path'")
    assert result == 'encoded_script'
