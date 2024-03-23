# file lib/ansible/utils/native_jinja.py:12-13
# lines [12, 13]
# branches []

import pytest
from ansible.utils.native_jinja import NativeJinjaText

def test_native_jinja_text_instantiation():
    # Test instantiation of NativeJinjaText
    test_string = "test"
    native_jinja_text = NativeJinjaText(test_string)
    
    # Verify that the instance is indeed of type NativeJinjaText
    assert isinstance(native_jinja_text, NativeJinjaText)
    
    # Verify that the content of the instance is correct
    assert str(native_jinja_text) == test_string
