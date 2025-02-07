# file: lib/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [70, 71, 73], "branches": []}
# gained: {"lines": [70, 71, 73], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_unsafe_bytes_decode():
    # Create an instance of AnsibleUnsafeBytes
    unsafe_bytes = AnsibleUnsafeBytes(b"unsafe data")

    # Call the decode method and check the result
    decoded_text = unsafe_bytes.decode('utf-8')
    assert isinstance(decoded_text, AnsibleUnsafeText)
    assert str(decoded_text) == "unsafe data"
    assert decoded_text.__UNSAFE__ is True
