# file: lib/ansible/plugins/shell/powershell.py:90-97
# asked: {"lines": [90, 92, 93, 94, 95, 97], "branches": [[94, 95], [94, 97]]}
# gained: {"lines": [90, 92, 93, 94, 95, 97], "branches": [[94, 95], [94, 97]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_get_remote_filename_ps1_extension(shell_module):
    filename = "script.ps1"
    result = shell_module.get_remote_filename(filename)
    assert result == "script.ps1"

def test_get_remote_filename_exe_extension(shell_module):
    filename = "script.exe"
    result = shell_module.get_remote_filename(filename)
    assert result == "script.exe"

def test_get_remote_filename_no_extension(shell_module):
    filename = "script"
    result = shell_module.get_remote_filename(filename)
    assert result == "script.ps1"

def test_get_remote_filename_other_extension(shell_module):
    filename = "script.txt"
    result = shell_module.get_remote_filename(filename)
    assert result == "script.ps1"

def test_get_remote_filename_whitespace(shell_module):
    filename = "  script.ps1  "
    result = shell_module.get_remote_filename(filename)
    assert result == "script.ps1"

def test_get_remote_filename_mixed_case_extension(shell_module):
    filename = "script.Ps1"
    result = shell_module.get_remote_filename(filename)
    assert result == "script.Ps1"
