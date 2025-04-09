# file: lib/ansible/plugins/callback/junit.py:251-253
# asked: {"lines": [251, 253], "branches": []}
# gained: {"lines": [251, 253], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_cleanse_string(callback_module):
    # Test with a normal string
    normal_string = "This is a test string."
    cleansed_string = callback_module._cleanse_string(normal_string)
    assert cleansed_string == normal_string

    # Test with a string containing surrogate escapes
    surrogate_string = "This is a test string with a surrogate escape: \udc80"
    cleansed_string = callback_module._cleanse_string(surrogate_string)
    assert cleansed_string == "This is a test string with a surrogate escape: �"

    # Test with an empty string
    empty_string = ""
    cleansed_string = callback_module._cleanse_string(empty_string)
    assert cleansed_string == empty_string

    # Test with a string containing non-ASCII characters
    non_ascii_string = "This is a test string with non-ASCII characters: üäöß"
    cleansed_string = callback_module._cleanse_string(non_ascii_string)
    assert cleansed_string == non_ascii_string
