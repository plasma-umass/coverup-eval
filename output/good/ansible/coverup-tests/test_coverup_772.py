# file lib/ansible/utils/unsafe_proxy.py:70-73
# lines [70, 71, 73]
# branches []

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_unsafe_bytes_decode():
    # Create an instance of AnsibleUnsafeBytes with some bytes
    unsafe_bytes = AnsibleUnsafeBytes(b"unsafe_data")

    # Decode the bytes and assert the result is an instance of AnsibleUnsafeText
    decoded_text = unsafe_bytes.decode('utf-8')
    assert isinstance(decoded_text, AnsibleUnsafeText)

    # Assert that the decoded text is the expected string
    assert decoded_text == "unsafe_data"

    # Test with additional arguments to cover all lines of the decode method
    decoded_text_with_args = unsafe_bytes.decode('utf-8', 'strict')
    assert decoded_text_with_args == "unsafe_data"
