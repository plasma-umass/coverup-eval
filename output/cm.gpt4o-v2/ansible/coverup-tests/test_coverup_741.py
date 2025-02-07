# file: lib/ansible/plugins/shell/powershell.py:99-102
# asked: {"lines": [99, 101, 102], "branches": []}
# gained: {"lines": [99, 101, 102], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash_with_slash(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='path/')
    result = shell_module.path_has_trailing_slash('path/')
    assert result is True

def test_path_has_trailing_slash_with_backslash(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='path\\')
    result = shell_module.path_has_trailing_slash('path\\')
    assert result is True

def test_path_has_trailing_slash_without_trailing_slash(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', return_value='path')
    result = shell_module.path_has_trailing_slash('path')
    assert result is False
