# file lib/ansible/plugins/shell/powershell.py:90-97
# lines [90, 92, 93, 94, 95, 97]
# branches ['94->95', '94->97']

import os
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_get_remote_filename_with_ps1_extension(shell_module):
    filename = shell_module.get_remote_filename('/path/to/script.ps1')
    assert filename == 'script.ps1'

def test_get_remote_filename_with_exe_extension(shell_module):
    filename = shell_module.get_remote_filename('/path/to/executable.exe')
    assert filename == 'executable.exe'

def test_get_remote_filename_with_different_extension(shell_module):
    filename = shell_module.get_remote_filename('/path/to/script.txt')
    assert filename == 'script.ps1'

def test_get_remote_filename_with_no_extension(shell_module):
    filename = shell_module.get_remote_filename('/path/to/script')
    assert filename == 'script.ps1'

def test_get_remote_filename_with_whitespace(shell_module):
    filename = shell_module.get_remote_filename('  /path/to/script  ')
    assert filename == 'script.ps1'
