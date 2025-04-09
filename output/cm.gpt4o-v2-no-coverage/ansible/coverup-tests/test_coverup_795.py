# file: lib/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [70, 71, 73], "branches": []}
# gained: {"lines": [70, 71, 73], "branches": []}

import pytest
from ansible.module_utils.six import binary_type
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

class AnsibleUnsafe(object):
    __UNSAFE__ = True

class TestAnsibleUnsafeBytes:
    
    def test_decode(self, mocker):
        # Mocking the super call to return a specific value
        mock_super = mocker.patch('ansible.utils.unsafe_proxy.super')
        mock_super.return_value.decode.return_value = 'decoded_text'
        
        # Creating an instance of AnsibleUnsafeBytes
        unsafe_bytes = AnsibleUnsafeBytes(b'some bytes')
        
        # Calling the decode method
        result = unsafe_bytes.decode('utf-8')
        
        # Asserting the result is an instance of AnsibleUnsafeText
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'decoded_text'
        
        # Asserting the decode method was called with the correct arguments
        mock_super.return_value.decode.assert_called_once_with('utf-8')
