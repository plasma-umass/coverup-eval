# file: lib/ansible/plugins/shell/powershell.py:135-146
# asked: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}
# gained: {"lines": [135, 139, 140, 141, 142, 143, 145, 146], "branches": [[140, 141], [140, 142], [142, 143], [142, 145]]}

import pytest
from unittest.mock import patch

# Assuming the ShellModule class is imported from ansible.plugins.shell.powershell
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_expand_user_tilde(shell_module):
    with patch.object(shell_module, '_unquote', return_value='~') as mock_unquote, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode:
        result = shell_module.expand_user('~')
        mock_unquote.assert_called_once_with('~')
        mock_encode.assert_called_once_with('Write-Output (Get-Location).Path')
        assert result == 'encoded_script'

def test_expand_user_tilde_backslash(shell_module):
    with patch.object(shell_module, '_unquote', return_value='~\\path') as mock_unquote, \
         patch.object(shell_module, '_escape', return_value='\\path') as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode:
        result = shell_module.expand_user('~\\path')
        mock_unquote.assert_called_once_with('~\\path')
        mock_escape.assert_called_once_with('\\path')
        mock_encode.assert_called_once_with("Write-Output ((Get-Location).Path + '\\path')")
        assert result == 'encoded_script'

def test_expand_user_other(shell_module):
    with patch.object(shell_module, '_unquote', return_value='/other/path') as mock_unquote, \
         patch.object(shell_module, '_escape', return_value='/other/path') as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode:
        result = shell_module.expand_user('/other/path')
        mock_unquote.assert_called_once_with('/other/path')
        mock_escape.assert_called_once_with('/other/path')
        mock_encode.assert_called_once_with("Write-Output '/other/path'")
        assert result == 'encoded_script'
