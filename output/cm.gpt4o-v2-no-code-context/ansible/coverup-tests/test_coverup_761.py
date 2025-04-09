# file: lib/ansible/plugins/shell/powershell.py:246-247
# asked: {"lines": [246, 247], "branches": []}
# gained: {"lines": [246, 247], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_wrap_for_exec(shell_module):
    cmd = 'echo Hello'
    expected_result = '& echo Hello; exit $LASTEXITCODE'
    result = shell_module.wrap_for_exec(cmd)
    assert result == expected_result
