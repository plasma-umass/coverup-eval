# file lib/ansible/plugins/shell/powershell.py:135-146
# lines [135, 139, 140, 141, 142, 143, 145, 146]
# branches ['140->141', '140->142', '142->143', '142->145']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_expand_user_tilde(shell_module):
    with patch.object(shell_module, '_unquote', return_value='~') as mock_unquote, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        result = shell_module.expand_user('~')
        mock_unquote.assert_called_once_with('~')
        mock_encode_script.assert_called_once_with('Write-Output (Get-Location).Path')
        assert result == 'encoded_script'

def test_expand_user_tilde_backslash(shell_module):
    with patch.object(shell_module, '_unquote', return_value='~\\') as mock_unquote, \
         patch.object(shell_module, '_escape', return_value='\\') as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        result = shell_module.expand_user('~\\')
        mock_unquote.assert_called_once_with('~\\')
        mock_escape.assert_called_once_with('\\')
        mock_encode_script.assert_called_once_with("Write-Output ((Get-Location).Path + '\\')")
        assert result == 'encoded_script'

def test_expand_user_other(shell_module):
    with patch.object(shell_module, '_unquote', return_value='C:\\Users\\user') as mock_unquote, \
         patch.object(shell_module, '_escape', return_value='C:\\Users\\user') as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        result = shell_module.expand_user('C:\\Users\\user')
        mock_unquote.assert_called_once_with('C:\\Users\\user')
        mock_escape.assert_called_once_with('C:\\Users\\user')
        mock_encode_script.assert_called_once_with("Write-Output 'C:\\Users\\user'")
        assert result == 'encoded_script'
