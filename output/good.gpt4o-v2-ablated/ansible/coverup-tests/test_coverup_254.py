# file: lib/ansible/plugins/shell/powershell.py:164-183
# asked: {"lines": [164, 165, 166, 182, 183], "branches": []}
# gained: {"lines": [164, 165, 166, 182, 183], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the ShellModule class is imported from ansible.plugins.shell.powershell
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_checksum_file_exists(monkeypatch, shell_module):
    path = "C:\\path\\to\\file.txt"
    
    def mock_escape(path):
        return path
    
    def mock_unquote(path):
        return path
    
    def mock_encode_script(script):
        assert "Test-Path -PathType Leaf" in script
        assert "System.Security.Cryptography.SHA1CryptoServiceProvider" in script
        return "encoded_script"
    
    monkeypatch.setattr(shell_module, "_escape", mock_escape)
    monkeypatch.setattr(shell_module, "_unquote", mock_unquote)
    monkeypatch.setattr(shell_module, "_encode_script", mock_encode_script)
    
    result = shell_module.checksum(path)
    assert result == "encoded_script"

def test_checksum_directory_exists(monkeypatch, shell_module):
    path = "C:\\path\\to\\directory"
    
    def mock_escape(path):
        return path
    
    def mock_unquote(path):
        return path
    
    def mock_encode_script(script):
        assert "Test-Path -PathType Container" in script
        assert "Write-Output \"3\"" in script
        return "encoded_script"
    
    monkeypatch.setattr(shell_module, "_escape", mock_escape)
    monkeypatch.setattr(shell_module, "_unquote", mock_unquote)
    monkeypatch.setattr(shell_module, "_encode_script", mock_encode_script)
    
    result = shell_module.checksum(path)
    assert result == "encoded_script"

def test_checksum_path_not_exists(monkeypatch, shell_module):
    path = "C:\\path\\to\\nonexistent"
    
    def mock_escape(path):
        return path
    
    def mock_unquote(path):
        return path
    
    def mock_encode_script(script):
        assert "Else" in script
        assert "Write-Output \"1\"" in script
        return "encoded_script"
    
    monkeypatch.setattr(shell_module, "_escape", mock_escape)
    monkeypatch.setattr(shell_module, "_unquote", mock_unquote)
    monkeypatch.setattr(shell_module, "_encode_script", mock_encode_script)
    
    result = shell_module.checksum(path)
    assert result == "encoded_script"
