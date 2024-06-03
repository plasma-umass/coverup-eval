# file lib/ansible/plugins/shell/powershell.py:107-108
# lines [107, 108]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_chown_not_implemented():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.chown(['dummy_path'], 'dummy_user')
    assert str(excinfo.value) == 'chown is not implemented for Powershell'
