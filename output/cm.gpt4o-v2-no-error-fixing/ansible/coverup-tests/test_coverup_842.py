# file: lib/ansible/plugins/callback/junit.py:251-253
# asked: {"lines": [253], "branches": []}
# gained: {"lines": [253], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule

@pytest.mark.parametrize("input_str,expected_output", [
    ("normal string", "normal string"),
    ("string with surrogate \udc80", "string with surrogate �"),
    ("string with multiple surrogates \udc80\udc81", "string with multiple surrogates ��"),
])
def test_cleanse_string(input_str, expected_output):
    callback = CallbackModule()
    result = callback._cleanse_string(input_str)
    assert result == expected_output
