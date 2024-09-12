# file: lib/ansible/plugins/shell/cmd.py:24-57
# asked: {"lines": [24, 27, 29, 31, 32, 35, 37, 43, 44, 46, 47, 52, 53, 55, 57], "branches": [[43, 44], [43, 46], [46, 47], [46, 52], [52, 53], [52, 57], [53, 52], [53, 55]]}
# gained: {"lines": [24, 27, 29, 31, 32, 35, 37, 43, 44, 46, 47, 52, 53, 55, 57], "branches": [[43, 44], [43, 46], [46, 47], [46, 52], [52, 53], [52, 57], [53, 52], [53, 55]]}

import pytest
from ansible.plugins.shell.cmd import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_quote_empty_string(shell_module):
    result = shell_module.quote("")
    assert result == '""'

def test_quote_no_unsafe_chars(shell_module):
    result = shell_module.quote("safe_string")
    assert result == "safe_string"

def test_quote_with_unsafe_chars(shell_module):
    unsafe_string = 'file &whoami.exe'
    result = shell_module.quote(unsafe_string)
    expected_result = '^"file ^&whoami.exe^"'
    assert result == expected_result

def test_quote_with_double_quote(shell_module):
    unsafe_string = 'file "name".exe'
    result = shell_module.quote(unsafe_string)
    expected_result = '^"file \\^"name\\^".exe^"'
    assert result == expected_result
