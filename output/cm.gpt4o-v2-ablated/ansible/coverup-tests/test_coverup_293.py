# file: lib/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [70, 71, 73], "branches": []}
# gained: {"lines": [70, 71, 73], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_unsafe_bytes_decode(monkeypatch):
    class MockAnsibleUnsafeText(str):
        def __new__(cls, value):
            return super(MockAnsibleUnsafeText, cls).__new__(cls, value)
    
    monkeypatch.setattr('ansible.utils.unsafe_proxy.AnsibleUnsafeText', MockAnsibleUnsafeText)
    
    unsafe_bytes = AnsibleUnsafeBytes(b'test')
    result = unsafe_bytes.decode('utf-8')
    
    assert isinstance(result, MockAnsibleUnsafeText)
    assert result == 'test'
