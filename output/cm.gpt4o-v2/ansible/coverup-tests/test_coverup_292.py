# file: lib/ansible/plugins/shell/powershell.py:249-258
# asked: {"lines": [249, 251, 252, 253, 254, 255, 256, 257, 258], "branches": [[253, 254], [253, 255], [256, 257], [256, 258]]}
# gained: {"lines": [249, 251, 252, 253, 254, 255, 256, 257, 258], "branches": [[253, 254], [253, 255], [256, 257], [256, 258]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_unquote_single_quotes(shell_module):
    result = shell_module._unquote("'test'")
    assert result == "test"

def test_unquote_double_quotes(shell_module):
    result = shell_module._unquote('"test"')
    assert result == "test"

def test_unquote_no_quotes(shell_module):
    result = shell_module._unquote('test')
    assert result == "test"

def test_unquote_empty_string(shell_module):
    result = shell_module._unquote('')
    assert result == ''

def test_unquote_none(shell_module):
    result = shell_module._unquote(None)
    assert result == ''
