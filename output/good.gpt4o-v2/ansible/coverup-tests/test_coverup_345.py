# file: lib/ansible/plugins/shell/powershell.py:135-146
# asked: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}
# gained: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

@pytest.fixture
def mock_unquote(mocker):
    return mocker.patch.object(ShellModule, '_unquote', side_effect=lambda x: x)

@pytest.fixture
def mock_escape(mocker):
    return mocker.patch.object(ShellModule, '_escape', side_effect=lambda x: x)

@pytest.fixture
def mock_encode_script(mocker):
    return mocker.patch.object(ShellModule, '_encode_script', side_effect=lambda x: x)

def test_expand_user_tilde(shell_module, mock_unquote, mock_escape, mock_encode_script):
    result = shell_module.expand_user('~')
    mock_unquote.assert_called_once_with('~')
    mock_escape.assert_not_called()
    mock_encode_script.assert_called_once_with('Write-Output (Get-Location).Path')
    assert result == 'Write-Output (Get-Location).Path'

def test_expand_user_tilde_backslash(shell_module, mock_unquote, mock_escape, mock_encode_script):
    result = shell_module.expand_user('~\\path')
    mock_unquote.assert_called_once_with('~\\path')
    mock_escape.assert_called_once_with('\\path')
    mock_encode_script.assert_called_once_with("Write-Output ((Get-Location).Path + '\\path')")
    assert result == "Write-Output ((Get-Location).Path + '\\path')"

def test_expand_user_other(shell_module, mock_unquote, mock_escape, mock_encode_script):
    result = shell_module.expand_user('/path')
    mock_unquote.assert_called_once_with('/path')
    mock_escape.assert_called_once_with('/path')
    mock_encode_script.assert_called_once_with("Write-Output '/path'")
    assert result == "Write-Output '/path'"
