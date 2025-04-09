# file: lib/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

def test_ansible_unsafe_text_encode():
    # Create an instance of AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText("test string")

    # Call the encode method
    encoded = unsafe_text.encode('utf-8')

    # Verify that the result is an instance of AnsibleUnsafeBytes
    assert isinstance(encoded, AnsibleUnsafeBytes)

    # Verify that the encoded value is correct
    assert encoded == b"test string"

    # Clean up
    del unsafe_text
    del encoded
