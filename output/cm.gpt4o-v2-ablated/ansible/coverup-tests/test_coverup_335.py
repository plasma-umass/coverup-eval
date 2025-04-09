# file: lib/ansible/plugins/shell/powershell.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chmod_raises_not_implemented_error():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.chmod(['dummy_path'], 0o755)
    assert str(excinfo.value) == 'chmod is not implemented for Powershell'
