# file: lib/ansible/plugins/shell/powershell.py:99-102
# asked: {"lines": [99, 101, 102], "branches": []}
# gained: {"lines": [99, 101, 102], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='C:\\path\\')

    assert shell_module.path_has_trailing_slash('C:\\path\\') is True
    shell_module._unquote.assert_called_once_with('C:\\path\\')

    mocker.patch.object(shell_module, '_unquote', return_value='C:\\path')
    assert shell_module.path_has_trailing_slash('C:\\path') is False
    shell_module._unquote.assert_called_with('C:\\path')

    mocker.patch.object(shell_module, '_unquote', return_value='/path/')
    assert shell_module.path_has_trailing_slash('/path/') is True
    shell_module._unquote.assert_called_with('/path/')

    mocker.patch.object(shell_module, '_unquote', return_value='/path')
    assert shell_module.path_has_trailing_slash('/path') is False
    shell_module._unquote.assert_called_with('/path')
