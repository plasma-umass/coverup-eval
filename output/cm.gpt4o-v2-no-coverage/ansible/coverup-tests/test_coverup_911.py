# file: lib/ansible/plugins/shell/powershell.py:260-264
# asked: {"lines": [260, 264], "branches": []}
# gained: {"lines": [260, 264], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_escape_single_quotes(shell_module):
    input_str = "This is a 'test' string"
    expected_output = "This is a ''test'' string"
    assert shell_module._escape(input_str) == expected_output

def test_escape_unicode_quotes(shell_module):
    input_str = "This is a \u2018test\u2019 string"
    expected_output = "This is a \u2018\u2018test\u2019\u2019 string"
    assert shell_module._escape(input_str) == expected_output

def test_escape_mixed_quotes(shell_module):
    input_str = "This is a 'test\u2018 string"
    expected_output = "This is a ''test\u2018\u2018 string"
    assert shell_module._escape(input_str) == expected_output

def test_escape_no_quotes(shell_module):
    input_str = "This is a test string"
    expected_output = "This is a test string"
    assert shell_module._escape(input_str) == expected_output
