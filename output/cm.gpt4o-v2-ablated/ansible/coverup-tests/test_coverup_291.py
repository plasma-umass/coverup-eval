# file: lib/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

def test_ansible_unsafe_text_encode():
    # Create an instance of AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText("test string")

    # Encode the text and verify the result is an instance of AnsibleUnsafeBytes
    encoded_text = unsafe_text.encode('utf-8')
    assert isinstance(encoded_text, AnsibleUnsafeBytes)
    assert encoded_text == b"test string"
