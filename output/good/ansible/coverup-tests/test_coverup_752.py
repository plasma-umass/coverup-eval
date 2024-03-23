# file lib/ansible/utils/unsafe_proxy.py:76-79
# lines [76, 77, 79]
# branches []

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

def test_ansible_unsafe_text_encode():
    # Create an instance of AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText("test")

    # Encode the text
    encoded_text = unsafe_text.encode('utf-8')

    # Check that the encoded text is an instance of AnsibleUnsafeBytes
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
    assert isinstance(encoded_text, AnsibleUnsafeBytes)

    # Check that the encoded text is correct
    assert encoded_text == b"test"
