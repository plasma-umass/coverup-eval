# file: lib/ansible/plugins/shell/powershell.py:110-111
# asked: {"lines": [110, 111], "branches": []}
# gained: {"lines": [110, 111], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_set_user_facl_not_implemented():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.set_user_facl(paths=['/some/path'], user='someuser', mode='rwx')
    assert str(excinfo.value) == 'set_user_facl is not implemented for Powershell'
