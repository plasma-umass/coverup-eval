# file: lib/ansible/plugins/shell/powershell.py:164-183
# asked: {"lines": [164, 165, 166, 182, 183], "branches": []}
# gained: {"lines": [164, 165, 166, 182, 183], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

@pytest.mark.parametrize("path, expected_script", [
    (r"C:\testfile.txt", '''
            If (Test-Path -PathType Leaf 'C:\\testfile.txt')
            {
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('C:\\testfile.txt', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }
            ElseIf (Test-Path -PathType Container 'C:\\testfile.txt')
            {
                Write-Output "3";
            }
            Else
            {
                Write-Output "1";
            }
        '''),
    (r"C:\testdir", '''
            If (Test-Path -PathType Leaf 'C:\\testdir')
            {
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('C:\\testdir', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }
            ElseIf (Test-Path -PathType Container 'C:\\testdir')
            {
                Write-Output "3";
            }
            Else
            {
                Write-Output "1";
            }
        '''),
    (r"C:\nonexistent", '''
            If (Test-Path -PathType Leaf 'C:\\nonexistent')
            {
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('C:\\nonexistent', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }
            ElseIf (Test-Path -PathType Container 'C:\\nonexistent')
            {
                Write-Output "3";
            }
            Else
            {
                Write-Output "1";
            }
        ''')
])
def test_checksum(shell_module, path, expected_script):
    with patch.object(ShellModule, '_escape', return_value=path), \
         patch.object(ShellModule, '_unquote', return_value=path), \
         patch.object(ShellModule, '_encode_script', return_value=expected_script) as mock_encode_script:
        
        result = shell_module.checksum(path)
        mock_encode_script.assert_called_once_with(expected_script)
        assert result == expected_script
