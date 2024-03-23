# file lib/ansible/plugins/shell/powershell.py:164-183
# lines [164, 165, 166, 182, 183]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell_module(mocker):
    mocker.patch.object(ShellModule, '_encode_script', side_effect=lambda x: x)
    mocker.patch.object(ShellModule, '_escape', side_effect=lambda x: x)
    mocker.patch.object(ShellModule, '_unquote', side_effect=lambda x: x)
    return ShellModule()

def test_checksum_leaf_path(powershell_shell_module, mocker):
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    script = powershell_shell_module.checksum('fake_path')
    assert "System.Security.Cryptography.SHA1CryptoServiceProvider" in script
    assert "fake_path" in script
    assert "Test-Path -PathType Leaf" in script

def test_checksum_container_path(powershell_shell_module, mocker):
    mocker.patch('os.path.isfile', return_value=False)
    mocker.patch('os.path.isdir', return_value=True)
    script = powershell_shell_module.checksum('fake_path')
    assert "Write-Output \"3\"" in script
    assert "fake_path" in script
    assert "Test-Path -PathType Container" in script

def test_checksum_nonexistent_path(powershell_shell_module, mocker):
    mocker.patch('os.path.isfile', return_value=False)
    mocker.patch('os.path.isdir', return_value=False)
    script = powershell_shell_module.checksum('fake_path')
    assert "Write-Output \"1\"" in script
    assert "fake_path" in script
    assert "Else" in script
