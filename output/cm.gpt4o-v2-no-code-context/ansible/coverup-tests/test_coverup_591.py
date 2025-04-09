# file: lib/ansible/plugins/shell/powershell.py:164-183
# asked: {"lines": [164, 165, 166, 182, 183], "branches": []}
# gained: {"lines": [164, 165, 166, 182, 183], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_checksum_file_exists(shell_module, mocker):
    path = "C:\\path\\to\\file.txt"
    escaped_path = shell_module._escape(shell_module._unquote(path))
    expected_script = f'''
            If (Test-Path -PathType Leaf '{escaped_path}')
            {{
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('{escaped_path}', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }}
            ElseIf (Test-Path -PathType Container '{escaped_path}')
            {{
                Write-Output "3";
            }}
            Else
            {{
                Write-Output "1";
            }}
        '''

    mocker.patch.object(shell_module, '_escape', return_value=escaped_path)
    mocker.patch.object(shell_module, '_unquote', return_value=path)
    mocker.patch.object(shell_module, '_encode_script', return_value="encoded_script")

    result = shell_module.checksum(path)

    shell_module._escape.assert_called_once_with(path)
    shell_module._unquote.assert_called_once_with(path)
    shell_module._encode_script.assert_called_once_with(expected_script)
    assert result == "encoded_script"

def test_checksum_directory_exists(shell_module, mocker):
    path = "C:\\path\\to\\directory"
    escaped_path = shell_module._escape(shell_module._unquote(path))
    expected_script = f'''
            If (Test-Path -PathType Leaf '{escaped_path}')
            {{
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('{escaped_path}', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }}
            ElseIf (Test-Path -PathType Container '{escaped_path}')
            {{
                Write-Output "3";
            }}
            Else
            {{
                Write-Output "1";
            }}
        '''

    mocker.patch.object(shell_module, '_escape', return_value=escaped_path)
    mocker.patch.object(shell_module, '_unquote', return_value=path)
    mocker.patch.object(shell_module, '_encode_script', return_value="encoded_script")

    result = shell_module.checksum(path)

    shell_module._escape.assert_called_once_with(path)
    shell_module._unquote.assert_called_once_with(path)
    shell_module._encode_script.assert_called_once_with(expected_script)
    assert result == "encoded_script"

def test_checksum_path_does_not_exist(shell_module, mocker):
    path = "C:\\path\\to\\nonexistent"
    escaped_path = shell_module._escape(shell_module._unquote(path))
    expected_script = f'''
            If (Test-Path -PathType Leaf '{escaped_path}')
            {{
                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;
                $fp = [System.IO.File]::Open('{escaped_path}', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);
                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();
                $fp.Dispose();
            }}
            ElseIf (Test-Path -PathType Container '{escaped_path}')
            {{
                Write-Output "3";
            }}
            Else
            {{
                Write-Output "1";
            }}
        '''

    mocker.patch.object(shell_module, '_escape', return_value=escaped_path)
    mocker.patch.object(shell_module, '_unquote', return_value=path)
    mocker.patch.object(shell_module, '_encode_script', return_value="encoded_script")

    result = shell_module.checksum(path)

    shell_module._escape.assert_called_once_with(path)
    shell_module._unquote.assert_called_once_with(path)
    shell_module._encode_script.assert_called_once_with(expected_script)
    assert result == "encoded_script"
