# file lib/ansible/utils/unsafe_proxy.py:70-73
# lines [70, 71, 73]
# branches []

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_unsafe_bytes_decode():
    # Create an instance of AnsibleUnsafeBytes with some binary data
    unsafe_bytes = AnsibleUnsafeBytes(b'test data')

    # Decode the binary data
    decoded_data = unsafe_bytes.decode('utf-8')

    # Verify that the decoded data is an instance of AnsibleUnsafeText
    assert isinstance(decoded_data, AnsibleUnsafeText)

    # Verify that the content of the decoded data is correct
    assert decoded_data == 'test data'
