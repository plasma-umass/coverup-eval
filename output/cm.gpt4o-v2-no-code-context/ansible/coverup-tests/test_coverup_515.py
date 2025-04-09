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
        'msg': 'Success'
    }
    caption = "COMMAND"
    
    expected_output = "localhost | COMMAND | rc=0 >>\nCommand executed successfullySuccess\n"
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output

def test_command_generic_msg_failure(callback_module):
    host = "localhost"
    result = {
        'rc': 1,
        'stdout': '',
        'stderr': 'Error occurred',
        'msg': 'Failure'
    }
    caption = "COMMAND"
    
    expected_output = "localhost | COMMAND | rc=1 >>\nError occurredFailure\n"
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output

def test_command_generic_msg_partial(callback_module):
    host = "localhost"
    result = {
        'rc': 0,
        'stdout': 'Partial output',
        'stderr': '',
        'msg': ''
    }
    caption = "COMMAND"
    
    expected_output = "localhost | COMMAND | rc=0 >>\nPartial output\n"
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output

def test_command_generic_msg_missing_fields(callback_module):
    host = "localhost"
    result = {}
    caption = "COMMAND"
    
    expected_output = "localhost | COMMAND | rc=-1 >>\n\n"
    output = callback_module._command_generic_msg(host, result, caption)
    
    assert output == expected_output
