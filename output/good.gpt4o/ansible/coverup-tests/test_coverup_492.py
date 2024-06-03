# file lib/ansible/plugins/callback/oneline.py:33-39
# lines [33, 34, 35, 36, 37, 39]
# branches ['35->36', '35->39']

import pytest
from ansible.plugins.callback.oneline import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg_with_stderr(callback_module):
    hostname = "test_host"
    result = {
        'stdout': 'output\nline2',
        'stderr': 'error\nline2',
        'rc': 1
    }
    caption = "test_caption"
    expected_output = "test_host | test_caption | rc=1 | (stdout) output\\nline2 (stderr) error\\nline2"
    
    actual_output = callback_module._command_generic_msg(hostname, result, caption)
    
    assert actual_output == expected_output

def test_command_generic_msg_without_stderr(callback_module):
    hostname = "test_host"
    result = {
        'stdout': 'output\nline2',
        'rc': 0
    }
    caption = "test_caption"
    expected_output = "test_host | test_caption | rc=0 | (stdout) output\\nline2"
    
    actual_output = callback_module._command_generic_msg(hostname, result, caption)
    
    assert actual_output == expected_output
