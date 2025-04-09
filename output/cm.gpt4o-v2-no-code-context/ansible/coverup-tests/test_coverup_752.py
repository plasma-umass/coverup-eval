# file: lib/ansible/plugins/shell/powershell.py:107-108
# asked: {"lines": [107, 108], "branches": []}
# gained: {"lines": [107, 108], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chown_not_implemented():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError, match='chown is not implemented for Powershell'):
        shell_module.chown(['dummy_path'], 'dummy_user')
