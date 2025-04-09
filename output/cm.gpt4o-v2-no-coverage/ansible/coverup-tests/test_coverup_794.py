# file: lib/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest
from ansible.module_utils.six import text_type, binary_type
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

def test_ansible_unsafe_text_encode():
    class MockAnsibleUnsafeText(AnsibleUnsafeText):
        def __new__(cls, content):
            instance = text_type.__new__(cls, content)
            return instance

    unsafe_text = MockAnsibleUnsafeText("unsafe_string")
    encoded = unsafe_text.encode('utf-8')

    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b"unsafe_string"
    assert encoded.__UNSAFE__ is True

def test_ansible_unsafe_bytes_decode():
    class MockAnsibleUnsafeBytes(AnsibleUnsafeBytes):
        def __new__(cls, content):
            instance = binary_type.__new__(cls, content)
            return instance

    unsafe_bytes = MockAnsibleUnsafeBytes(b"unsafe_bytes")
    decoded = unsafe_bytes.decode('utf-8')

    assert isinstance(decoded, text_type)
    assert decoded == "unsafe_bytes"
    assert decoded.__UNSAFE__ is True
