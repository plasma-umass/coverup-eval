# file: lib/ansible/plugins/shell/powershell.py:164-183
# asked: {"lines": [164, 165, 166, 182, 183], "branches": []}
# gained: {"lines": [164, 165, 166, 182, 183], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_checksum_file_exists(shell_module):
    path = "C:\\path\\to\\file.txt"
    unquoted_path = path
    escaped_path = path

    with patch.object(shell_module, '_unquote', return_value=unquoted_path) as mock_unquote, \
         patch.object(shell_module, '_escape', return_value=escaped_path) as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value="encoded_script") as mock_encode_script:
        
        result = shell_module.checksum(path)
        
        mock_unquote.assert_called_once_with(path)
        mock_escape.assert_called_once_with(unquoted_path)
        mock_encode_script.assert_called_once()
        assert result == "encoded_script"

def test_checksum_directory_exists(shell_module):
    path = "C:\\path\\to\\directory"
    unquoted_path = path
    escaped_path = path

    with patch.object(shell_module, '_unquote', return_value=unquoted_path) as mock_unquote, \
         patch.object(shell_module, '_escape', return_value=escaped_path) as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value="encoded_script") as mock_encode_script:
        
        result = shell_module.checksum(path)
        
        mock_unquote.assert_called_once_with(path)
        mock_escape.assert_called_once_with(unquoted_path)
        mock_encode_script.assert_called_once()
        assert result == "encoded_script"

def test_checksum_path_not_exists(shell_module):
    path = "C:\\path\\to\\nonexistent"
    unquoted_path = path
    escaped_path = path

    with patch.object(shell_module, '_unquote', return_value=unquoted_path) as mock_unquote, \
         patch.object(shell_module, '_escape', return_value=escaped_path) as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value="encoded_script") as mock_encode_script:
        
        result = shell_module.checksum(path)
        
        mock_unquote.assert_called_once_with(path)
        mock_escape.assert_called_once_with(unquoted_path)
        mock_encode_script.assert_called_once()
        assert result == "encoded_script"
