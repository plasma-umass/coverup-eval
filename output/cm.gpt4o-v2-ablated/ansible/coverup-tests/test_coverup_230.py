# file: lib/ansible/plugins/callback/minimal.py:33-41
# asked: {"lines": [33, 36, 37, 38, 39, 41], "branches": []}
# gained: {"lines": [33, 36, 37, 38, 39, 41], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg_success(callback_module):
    host = "localhost"
    result = {
        'rc': 0,
        'stdout': 'Command executed successfully',
        'stderr': '',
        'msg': ''
    }
    caption = "SUCCESS"
    expected_output = "localhost | SUCCESS | rc=0 >>\nCommand executed successfully\n"
    
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output

def test_command_generic_msg_failure(callback_module):
    host = "localhost"
    result = {
        'rc': 1,
        'stdout': '',
        'stderr': 'Error occurred',
        'msg': 'Some error message'
    }
    caption = "FAILURE"
    expected_output = "localhost | FAILURE | rc=1 >>\nError occurredSome error message\n"
    
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output

def test_command_generic_msg_default_rc(callback_module):
    host = "localhost"
    result = {
        'stdout': 'Command executed with default rc',
        'stderr': '',
        'msg': ''
    }
    caption = "DEFAULT_RC"
    expected_output = "localhost | DEFAULT_RC | rc=-1 >>\nCommand executed with default rc\n"
    
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output
