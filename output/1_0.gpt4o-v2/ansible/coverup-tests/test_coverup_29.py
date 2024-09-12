# file: lib/ansible/plugins/shell/sh.py:46-78
# asked: {"lines": [46, 69, 70, 71, 72, 73, 76, 77, 78], "branches": []}
# gained: {"lines": [46, 69, 70, 71, 72, 73, 76, 77, 78], "branches": []}

import pytest
from ansible.plugins.shell.sh import ShellModule
from unittest.mock import patch
import os

@pytest.fixture
def shell_module():
    return ShellModule()

def test_checksum_file_exists(shell_module, tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("content")
    
    with patch("ansible.plugins.shell.sh.shlex_quote", return_value=str(test_file)):
        cmd = shell_module.checksum(str(test_file), "python3")
        assert "test_file.txt" in cmd
        assert "import hashlib" in cmd

def test_checksum_file_not_readable(shell_module, tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("content")
    test_file.chmod(0o000)  # No permissions

    with patch("ansible.plugins.shell.sh.shlex_quote", return_value=str(test_file)):
        cmd = shell_module.checksum(str(test_file), "python3")
        assert "rc=2" in cmd

def test_checksum_file_is_directory(shell_module, tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    with patch("ansible.plugins.shell.sh.shlex_quote", return_value=str(test_dir)):
        cmd = shell_module.checksum(str(test_dir), "python3")
        assert "rc=3" in cmd

def test_checksum_no_python_interpreter(shell_module, tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("content")

    with patch("ansible.plugins.shell.sh.shlex_quote", return_value=str(test_file)):
        cmd = shell_module.checksum(str(test_file), "nonexistent_python")
        assert "rc=4" in cmd

def test_checksum_unknown_error(shell_module, tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("content")

    with patch("ansible.plugins.shell.sh.shlex_quote", return_value=str(test_file)):
        cmd = shell_module.checksum(str(test_file), "python3")
        assert "echo '0  '" in cmd
