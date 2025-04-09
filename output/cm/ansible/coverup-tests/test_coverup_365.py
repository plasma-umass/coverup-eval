# file lib/ansible/plugins/shell/powershell.py:135-146
# lines [135, 139, 140, 141, 142, 143, 145, 146]
# branches ['140->141', '140->142', '142->143', '142->145']

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell():
    return ShellModule()

def test_expand_user_tilde(powershell_shell, mocker):
    mocker.patch.object(powershell_shell, '_unquote', return_value='~')
    mocker.patch.object(powershell_shell, '_encode_script')
    powershell_shell.expand_user('~')
    powershell_shell._encode_script.assert_called_once_with('Write-Output (Get-Location).Path')

def test_expand_user_tilde_with_backslash(powershell_shell, mocker):
    mocker.patch.object(powershell_shell, '_unquote', return_value='~\\path')
    mocker.patch.object(powershell_shell, '_escape', side_effect=lambda x: x)
    mocker.patch.object(powershell_shell, '_encode_script')
    powershell_shell.expand_user('~\\path')
    powershell_shell._encode_script.assert_called_once_with("Write-Output ((Get-Location).Path + '\\path')")

def test_expand_user_other_path(powershell_shell, mocker):
    mocker.patch.object(powershell_shell, '_unquote', return_value='C:\\Users\\username')
    mocker.patch.object(powershell_shell, '_escape', side_effect=lambda x: x)
    mocker.patch.object(powershell_shell, '_encode_script')
    powershell_shell.expand_user('C:\\Users\\username')
    powershell_shell._encode_script.assert_called_once_with("Write-Output 'C:\\Users\\username'")
