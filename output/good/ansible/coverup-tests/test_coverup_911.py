# file lib/ansible/plugins/shell/powershell.py:246-247
# lines [246, 247]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell():
    return ShellModule()

def test_wrap_for_exec(powershell_shell):
    cmd = "Get-Process"
    wrapped_cmd = powershell_shell.wrap_for_exec(cmd)
    assert wrapped_cmd == "& Get-Process; exit $LASTEXITCODE"
