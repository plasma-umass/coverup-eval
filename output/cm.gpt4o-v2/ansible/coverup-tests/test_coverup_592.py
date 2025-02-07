# file: lib/ansible/plugins/callback/minimal.py:33-41
# asked: {"lines": [33, 36, 37, 38, 39, 41], "branches": []}
# gained: {"lines": [33, 36, 37, 38, 39, 41], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg(callback_module):
    host = "localhost"
    result = {
        'rc': 0,
        'stdout': 'command output',
        'stderr': 'error output',
        'msg': 'some message'
    }
    caption = "test caption"
    
    expected_output = "localhost | test caption | rc=0 >>\ncommand outputerror outputsome message\n"
    actual_output = callback_module._command_generic_msg(host, result, caption)
    
    assert actual_output == expected_output

def test_command_generic_msg_missing_fields(callback_module):
    host = "localhost"
    result = {}
    caption = "test caption"
    
    expected_output = "localhost | test caption | rc=-1 >>\n\n"
    actual_output = callback_module._command_generic_msg(host, result, caption)
    
    assert actual_output == expected_output
