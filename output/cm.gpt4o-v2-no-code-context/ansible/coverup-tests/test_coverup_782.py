# file: lib/ansible/plugins/callback/junit.py:251-253
# asked: {"lines": [251, 253], "branches": []}
# gained: {"lines": [251, 253], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_cleanse_string_surrogateescape(callback_module):
    input_string = 'test\uDC80string'
    expected_output = 'test�string'
    result = callback_module._cleanse_string(input_string)
    assert result == expected_output

def test_cleanse_string_normal(callback_module):
    input_string = 'normalstring'
    expected_output = 'normalstring'
    result = callback_module._cleanse_string(input_string)
    assert result == expected_output
