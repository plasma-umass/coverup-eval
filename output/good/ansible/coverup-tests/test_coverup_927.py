# file lib/ansible/plugins/callback/junit.py:251-253
# lines [251, 253]
# branches []

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_cleanse_string_with_surrogateescape(callback_module, tmp_path):
    # Create a string with a surrogateescape error
    bad_string = "This is a bad string \udcc3"
    # Call the _cleanse_string method
    cleansed_string = callback_module._cleanse_string(bad_string)
    # Check that the surrogateescape was replaced with the unicode replacement character
    assert '\ufffd' in cleansed_string
    assert bad_string not in cleansed_string

    # Clean up after the test
    del callback_module
