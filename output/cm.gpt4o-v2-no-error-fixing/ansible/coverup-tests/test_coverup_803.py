# file: lib/ansible/utils/hashing.py:45-51
# asked: {"lines": [48, 49, 50, 51], "branches": []}
# gained: {"lines": [48, 49, 50, 51], "branches": []}

import pytest
from hashlib import sha1
from ansible.module_utils._text import to_bytes
from ansible.utils.hashing import secure_hash_s

def test_secure_hash_s():
    data = "test data"
    expected_hash = sha1(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_nonstring():
    data = 12345  # non-string input
    expected_hash = sha1(to_bytes(str(data), errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_bytes():
    data = b"test data"
    expected_hash = sha1(data).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_with_custom_hash_func():
    from hashlib import md5
    data = "test data"
    expected_hash = md5(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data, hash_func=md5) == expected_hash
