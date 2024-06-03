# file lib/ansible/plugins/shell/powershell.py:246-247
# lines [246, 247]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_wrap_for_exec():
    shell_module = ShellModule()
    cmd = 'echo Hello'
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    
    assert wrapped_cmd == '& echo Hello; exit $LASTEXITCODE'
