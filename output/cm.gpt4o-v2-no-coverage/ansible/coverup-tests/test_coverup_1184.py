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
    expected_output = "localhost | test command | rc=0 >>\ncommand outputerror outputadditional message\n"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output

def test_command_generic_msg_missing_fields(callback_module):
    host = "localhost"
    result = {}
    caption = "test command"
    expected_output = "localhost | test command | rc=-1 >>\n\n"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output

def test_command_generic_msg_partial_fields(callback_module):
    host = "localhost"
    result = {
        "stdout": "command output"
    }
    caption = "test command"
    expected_output = "localhost | test command | rc=-1 >>\ncommand output\n"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output

    result = {
        "stderr": "error output"
    }
    expected_output = "localhost | test command | rc=-1 >>\nerror output\n"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output

    result = {
        "msg": "additional message"
    }
    expected_output = "localhost | test command | rc=-1 >>\nadditional message\n"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output
