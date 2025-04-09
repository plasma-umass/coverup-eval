# file lib/ansible/plugins/callback/minimal.py:33-41
# lines [33, 36, 37, 38, 39, 41]
# branches []

import pytest
from ansible.plugins.callback import minimal

@pytest.fixture
def minimal_callback():
    return minimal.CallbackModule()

def test_command_generic_msg(minimal_callback):
    host = "localhost"
    caption = "Test Caption"
    result = {
        'rc': 0,
        'stdout': 'Test stdout',
        'stderr': 'Test stderr',
        'msg': 'Test message'
    }

    expected_output = "localhost | Test Caption | rc=0 >>\nTest stdoutTest stderrTest message\n"
    output = minimal_callback._command_generic_msg(host, result, caption)
    assert output == expected_output
