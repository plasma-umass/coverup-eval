# file: lib/ansible/plugins/shell/powershell.py:260-264
# asked: {"lines": [260, 264], "branches": []}
# gained: {"lines": [260, 264], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_escape_single_quote(shell_module):
    input_value = "It's a test"
    expected_output = "It''s a test"
    assert shell_module._escape(input_value) == expected_output

def test_escape_unicode_quotes(shell_module):
    input_value = "Test\u2018Test\u2019Test\u201aTest\u201b"
    expected_output = "Test\u2018\u2018Test\u2019\u2019Test\u201a\u201aTest\u201b\u201b"
    assert shell_module._escape(input_value) == expected_output
