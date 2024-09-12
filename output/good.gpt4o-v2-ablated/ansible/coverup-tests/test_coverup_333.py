# file: lib/ansible/plugins/shell/powershell.py:107-108
# asked: {"lines": [107, 108], "branches": []}
# gained: {"lines": [107, 108], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chown_raises_not_implemented_error():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.chown(['some_path'], 'some_user')
    assert str(excinfo.value) == 'chown is not implemented for Powershell'
