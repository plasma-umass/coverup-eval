# file: lib/ansible/plugins/shell/powershell.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chmod_raises_not_implemented_error():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError, match='chmod is not implemented for Powershell'):
        shell_module.chmod(['dummy_path'], 0o755)
