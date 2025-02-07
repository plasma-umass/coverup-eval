# file: lib/ansible/plugins/shell/powershell.py:77-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_env_prefix(shell_module):
    result = shell_module.env_prefix()
    assert result == ""
