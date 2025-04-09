# file: lib/ansible/plugins/shell/powershell.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chmod_not_implemented():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError, match='chmod is not implemented for Powershell'):
        shell_module.chmod(['some_path'], 0o777)
