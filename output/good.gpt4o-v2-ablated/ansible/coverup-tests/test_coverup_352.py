# file: lib/ansible/plugins/callback/junit.py:251-253
# asked: {"lines": [251, 253], "branches": []}
# gained: {"lines": [251, 253], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_cleanse_string_normal(callback_module):
    input_str = "normal string"
    expected_output = "normal string"
    assert callback_module._cleanse_string(input_str) == expected_output

def test_cleanse_string_with_surrogate(callback_module):
    input_str = "string with surrogate \udc80"
    expected_output = "string with surrogate �"
    assert callback_module._cleanse_string(input_str) == expected_output

def test_cleanse_string_with_bytes(callback_module):
    input_bytes = b"byte string"
    expected_output = "byte string"
    assert callback_module._cleanse_string(input_bytes) == expected_output

def test_cleanse_string_with_special_chars(callback_module):
    input_str = "special chars \u20ac \u00a3"
    expected_output = "special chars € £"
    assert callback_module._cleanse_string(input_str) == expected_output
