# file lib/ansible/plugins/callback/oneline.py:33-39
# lines [33, 34, 35, 36, 37, 39]
# branches ['35->36', '35->39']

import pytest
from ansible.plugins.callback.oneline import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg_with_stderr(callback_module):
    hostname = 'localhost'
    caption = 'COMMAND'
    result = {
        'stdout': 'output here',
        'stderr': 'error here',
        'rc': 0
    }
    expected_output = "localhost | COMMAND | rc=0 | (stdout) output here (stderr) error here"
    output = callback_module._command_generic_msg(hostname, result, caption)
    assert output == expected_output

def test_command_generic_msg_without_stderr(callback_module):
    hostname = 'localhost'
    caption = 'COMMAND'
    result = {
        'stdout': 'output here',
        'rc': 0
    }
    expected_output = "localhost | COMMAND | rc=0 | (stdout) output here"
    output = callback_module._command_generic_msg(hostname, result, caption)
    assert output == expected_output
