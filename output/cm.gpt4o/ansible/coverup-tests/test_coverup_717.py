# file lib/ansible/utils/unsafe_proxy.py:76-79
# lines [76, 77, 79]
# branches []

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

def test_ansible_unsafe_text_encode():
    # Create an instance of AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText("test string")

    # Encode the text and check the type and value
    encoded_text = unsafe_text.encode('utf-8')
    assert isinstance(encoded_text, AnsibleUnsafeBytes)
    assert encoded_text == b"test string"

    # Ensure the unsafe context is maintained
    assert isinstance(encoded_text, AnsibleUnsafe)

    # Clean up
    del unsafe_text
    del encoded_text
