# file: lib/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [70, 71, 73], "branches": []}
# gained: {"lines": [70, 71, 73], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_unsafe_bytes_decode():
    # Create an instance of AnsibleUnsafeBytes
    unsafe_bytes = AnsibleUnsafeBytes(b"test string")

    # Decode the bytes
    decoded_text = unsafe_bytes.decode("utf-8")

    # Verify that the result is an instance of AnsibleUnsafeText
    assert isinstance(decoded_text, AnsibleUnsafeText)
    assert decoded_text == "test string"
