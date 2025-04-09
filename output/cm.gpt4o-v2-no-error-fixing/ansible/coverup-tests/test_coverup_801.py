# file: lib/ansible/plugins/callback/minimal.py:33-41
# asked: {"lines": [36, 37, 38, 39, 41], "branches": []}
# gained: {"lines": [36, 37, 38, 39, 41], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg_all_fields(callback_module):
    host = "localhost"
    result = {
        "rc": 0,
        "stdout": "command output",
        "stderr": "error output",
        "msg": "additional message"
    }
    caption = "test command"
    
    expected_output = (
        "localhost | test command | rc=0 >>\n"
        "command output"
        "error output"
        "additional message\n"
    )
    
    output = callback_module._command_generic_msg(host, result, caption)
    assert output == expected_output

def test_command_generic_msg_missing_fields(callback_module):
    host = "localhost"
    result = {}
    caption = "test command"
    
    expected_output = (
        "localhost | test command | rc=-1 >>\n\n"
    )
    
    output = callback_module._command_generic_msg(host, result, caption)
    assert output == expected_output
