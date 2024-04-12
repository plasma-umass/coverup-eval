# file lib/ansible/utils/unsafe_proxy.py:82-83
# lines [82, 83]
# branches []

import pytest
from ansible.utils.unsafe_proxy import NativeJinjaUnsafeText, AnsibleUnsafeText

def test_NativeJinjaUnsafeText_inheritance():
    # Verify that NativeJinjaUnsafeText inherits from AnsibleUnsafeText
    assert issubclass(NativeJinjaUnsafeText, AnsibleUnsafeText)

    # Create an instance of NativeJinjaUnsafeText and check its type
    unsafe_text_instance = NativeJinjaUnsafeText("some unsafe text")
    assert isinstance(unsafe_text_instance, NativeJinjaUnsafeText)
    assert isinstance(unsafe_text_instance, AnsibleUnsafeText)

    # Check that the text is correctly stored in the instance
    assert unsafe_text_instance == "some unsafe text"
