# file lib/ansible/plugins/shell/powershell.py:113-118
# lines [113, 114, 115, 116, 118]
# branches ['115->116', '115->118']

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell(mocker):
    mocker.patch('ansible.plugins.shell.powershell.ShellModule.__init__', return_value=None)
    shell_module = ShellModule()
    shell_module._encode_script = lambda script: script
    return shell_module

def test_remove_non_recursive(powershell_shell):
    path = "C:\\path\\to\\remove"
    expected_script = "Remove-Item 'C:\\path\\to\\remove' -Force;"
    removal_script = powershell_shell.remove(path)
    assert removal_script == expected_script

def test_remove_recursive(powershell_shell):
    path = "C:\\path\\to\\remove"
    expected_script = "Remove-Item 'C:\\path\\to\\remove' -Force -Recurse;"
    removal_script = powershell_shell.remove(path, recurse=True)
    assert removal_script == expected_script
