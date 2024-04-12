# file lib/ansible/plugins/shell/powershell.py:60-76
# lines [60, 65, 67, 69, 70, 73]
# branches []

import pytest

from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell_module():
    return ShellModule()

def test_shell_module_properties(powershell_shell_module):
    assert powershell_shell_module.COMPATIBLE_SHELLS == frozenset()
    assert powershell_shell_module.SHELL_FAMILY == 'powershell'
    assert powershell_shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert powershell_shell_module._SHELL_AND == ';'
    assert powershell_shell_module._IS_WINDOWS is True
