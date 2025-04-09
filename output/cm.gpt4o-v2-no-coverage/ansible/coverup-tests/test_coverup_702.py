# file: lib/ansible/utils/hashing.py:45-51
# asked: {"lines": [45, 48, 49, 50, 51], "branches": []}
# gained: {"lines": [45, 48, 49, 50, 51], "branches": []}

import pytest
from hashlib import sha1
from ansible.module_utils._text import to_bytes
from ansible.utils.hashing import secure_hash_s

def test_secure_hash_s_default_hash_func():
    data = "test data"
    expected_hash = sha1(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_custom_hash_func(monkeypatch):
    class MockHash:
        def __init__(self):
            self.data = b""
        def update(self, data):
            self.data += data
        def hexdigest(self):
            return "mockedhash"

    def mock_hash_func():
        return MockHash()

    data = "test data"
    monkeypatch.setattr('hashlib.sha1', mock_hash_func)
    assert secure_hash_s(data, hash_func=mock_hash_func) == "mockedhash"

def test_secure_hash_s_nonstring_data():
    data = 12345
    expected_hash = sha1(to_bytes(str(data), errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_bytes_data():
    data = b"test data"
    expected_hash = sha1(data).hexdigest()
    assert secure_hash_s(data) == expected_hash
