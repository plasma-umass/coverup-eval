# file: lib/ansible/plugins/shell/powershell.py:90-97
# asked: {"lines": [90, 92, 93, 94, 95, 97], "branches": [[94, 95], [94, 97]]}
# gained: {"lines": [90, 92, 93, 94, 95, 97], "branches": [[94, 95], [94, 97]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_get_remote_filename_ps1_extension(shell_module):
    result = shell_module.get_remote_filename("script")
    assert result == "script.ps1"

def test_get_remote_filename_with_ps1_extension(shell_module):
    result = shell_module.get_remote_filename("script.ps1")
    assert result == "script.ps1"

def test_get_remote_filename_with_exe_extension(shell_module):
    result = shell_module.get_remote_filename("script.exe")
    assert result == "script.exe"

def test_get_remote_filename_with_other_extension(shell_module):
    result = shell_module.get_remote_filename("script.txt")
    assert result == "script.ps1"
