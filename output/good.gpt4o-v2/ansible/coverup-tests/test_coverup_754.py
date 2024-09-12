# file: lib/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes
from ansible.module_utils.six import text_type

def test_ansible_unsafe_text_encode():
    # Create an instance of AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText("unsafe_string")

    # Mock the encode method to ensure it returns a known value
    encoded_value = unsafe_text.encode('utf-8')

    # Verify that the returned value is an instance of AnsibleUnsafeBytes
    assert isinstance(encoded_value, AnsibleUnsafeBytes)

    # Verify that the encoded value is correct
    assert encoded_value == AnsibleUnsafeBytes(b"unsafe_string")

    # Clean up
    del unsafe_text
    del encoded_value
