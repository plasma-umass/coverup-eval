# file lib/ansible/plugins/shell/powershell.py:260-264
# lines [260, 264]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell_module():
    return ShellModule()

def test_escape_special_chars(powershell_shell_module):
    # Test escaping of special characters
    special_chars = "test'‘’‚‛"
    escaped_chars = powershell_shell_module._escape(special_chars)
    assert escaped_chars == "test''‘‘’’‚‚‛‛"

    # Test with no special characters to escape
    no_special_chars = "test"
    escaped_no_chars = powershell_shell_module._escape(no_special_chars)
    assert escaped_no_chars == "test"

    # Test with empty string
    empty_string = ""
    escaped_empty = powershell_shell_module._escape(empty_string)
    assert escaped_empty == ""
