# file lib/ansible/plugins/shell/powershell.py:99-102
# lines [99, 101, 102]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash_with_forward_slash(shell_module):
    path = "C:/some/path/"
    assert shell_module.path_has_trailing_slash(path) == True

def test_path_has_trailing_slash_with_backward_slash(shell_module):
    path = "C:\\some\\path\\"
    assert shell_module.path_has_trailing_slash(path) == True

def test_path_has_trailing_slash_without_slash(shell_module):
    path = "C:/some/path"
    assert shell_module.path_has_trailing_slash(path) == False

def test_path_has_trailing_slash_with_quoted_path(shell_module):
    path = '"C:/some/path/"'
    assert shell_module.path_has_trailing_slash(path) == True

def test_path_has_trailing_slash_with_quoted_path_no_slash(shell_module):
    path = '"C:/some/path"'
    assert shell_module.path_has_trailing_slash(path) == False
