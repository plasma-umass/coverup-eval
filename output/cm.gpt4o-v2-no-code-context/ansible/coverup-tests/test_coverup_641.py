# file: lib/ansible/plugins/shell/powershell.py:99-102
# asked: {"lines": [99, 101, 102], "branches": []}
# gained: {"lines": [99, 101, 102], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash_with_forward_slash(shell_module):
    path = "C:/some/path/"
    result = shell_module.path_has_trailing_slash(path)
    assert result is True

def test_path_has_trailing_slash_with_backslash(shell_module):
    path = "C:\\some\\path\\"
    result = shell_module.path_has_trailing_slash(path)
    assert result is True

def test_path_has_no_trailing_slash(shell_module):
    path = "C:/some/path"
    result = shell_module.path_has_trailing_slash(path)
    assert result is False

def test_path_has_no_trailing_backslash(shell_module):
    path = "C:\\some\\path"
    result = shell_module.path_has_trailing_slash(path)
    assert result is False

def test_path_has_trailing_slash_with_quotes(shell_module, mocker):
    path = '"C:/some/path/"'
    mocker.patch.object(shell_module, '_unquote', return_value='C:/some/path/')
    result = shell_module.path_has_trailing_slash(path)
    assert result is True

def test_path_has_trailing_backslash_with_quotes(shell_module, mocker):
    path = '"C:\\some\\path\\"'
    mocker.patch.object(shell_module, '_unquote', return_value='C:\\some\\path\\')
    result = shell_module.path_has_trailing_slash(path)
    assert result is True
