# file lib/ansible/plugins/shell/powershell.py:110-111
# lines [110, 111]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_set_user_facl_not_implemented():
    shell_module = ShellModule()

    with pytest.raises(NotImplementedError) as exc_info:
        shell_module.set_user_facl(paths=[], user='someuser', mode='rwx')

    assert str(exc_info.value) == 'set_user_facl is not implemented for Powershell'
