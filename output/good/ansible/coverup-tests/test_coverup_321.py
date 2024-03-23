# file lib/ansible/plugins/shell/powershell.py:249-258
# lines [249, 251, 252, 253, 254, 255, 256, 257, 258]
# branches ['253->254', '253->255', '256->257', '256->258']

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_unquote_with_single_quotes(shell_module):
    assert shell_module._unquote("'single quoted string'") == "single quoted string"

def test_unquote_with_double_quotes(shell_module):
    assert shell_module._unquote('"double quoted string"') == "double quoted string"

def test_unquote_without_quotes(shell_module):
    assert shell_module._unquote("no quotes string") == "no quotes string"

def test_unquote_with_leading_and_trailing_spaces_single_quotes(shell_module):
    assert shell_module._unquote("   '  spaced single quoted string  '   ") == "  spaced single quoted string  "

def test_unquote_with_leading_and_trailing_spaces_double_quotes(shell_module):
    assert shell_module._unquote('   "  spaced double quoted string  "   ') == "  spaced double quoted string  "

def test_unquote_with_none(shell_module):
    assert shell_module._unquote(None) == ""
