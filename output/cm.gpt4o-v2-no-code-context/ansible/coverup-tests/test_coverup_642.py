# file: lib/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

def test_ansible_unsafe_text_encode():
    unsafe_text = AnsibleUnsafeText("unsafe string")
    encoded_text = unsafe_text.encode('utf-8')
    
    assert isinstance(encoded_text, AnsibleUnsafeBytes)
    assert encoded_text == b"unsafe string"
