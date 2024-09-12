# file: lib/ansible/utils/hashing.py:45-51
# asked: {"lines": [45, 48, 49, 50, 51], "branches": []}
# gained: {"lines": [45, 48, 49, 50, 51], "branches": []}

import pytest
from hashlib import sha1
from ansible.utils.hashing import secure_hash_s

def test_secure_hash_s_with_string():
    data = "test string"
    expected_hash = sha1(data.encode('utf-8')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_bytes():
    data = b"test bytes"
    expected_hash = sha1(data).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_nonstring():
    data = 12345
    expected_hash = sha1(str(data).encode('utf-8')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_surrogateescape(monkeypatch):
    data = "test \udc80 string"
    def mock_to_bytes(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        return obj.encode(encoding, 'surrogateescape')
    monkeypatch.setattr('ansible.module_utils._text.to_bytes', mock_to_bytes)
    expected_hash = sha1(data.encode('utf-8', 'surrogateescape')).hexdigest()
    assert secure_hash_s(data) == expected_hash
