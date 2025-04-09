# file: lib/ansible/plugins/callback/oneline.py:33-39
# asked: {"lines": [33, 34, 35, 36, 37, 39], "branches": [[35, 36], [35, 39]]}
# gained: {"lines": [33, 34, 35, 36, 37, 39], "branches": [[35, 36], [35, 39]]}

import pytest
from ansible.plugins.callback.oneline import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_command_generic_msg_no_stderr(callback_module):
    hostname = "localhost"
    result = {"stdout": "output", "rc": 0}
    caption = "test"
    expected = "localhost | test | rc=0 | (stdout) output"
    assert callback_module._command_generic_msg(hostname, result, caption) == expected

def test_command_generic_msg_with_stderr(callback_module):
    hostname = "localhost"
    result = {"stdout": "output", "stderr": "error", "rc": 1}
    caption = "test"
    expected = "localhost | test | rc=1 | (stdout) output (stderr) error"
    assert callback_module._command_generic_msg(hostname, result, caption) == expected

def test_command_generic_msg_no_stdout(callback_module):
    hostname = "localhost"
    result = {"stderr": "error", "rc": 1}
    caption = "test"
    expected = "localhost | test | rc=1 | (stdout)  (stderr) error"
    assert callback_module._command_generic_msg(hostname, result, caption) == expected

def test_command_generic_msg_no_rc(callback_module):
    hostname = "localhost"
    result = {"stdout": "output", "stderr": "error"}
    caption = "test"
    expected = "localhost | test | rc=-1 | (stdout) output (stderr) error"
    assert callback_module._command_generic_msg(hostname, result, caption) == expected
