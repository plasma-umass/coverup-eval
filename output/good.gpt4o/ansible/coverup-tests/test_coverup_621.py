# file lib/ansible/utils/hashing.py:45-51
# lines [45, 48, 49, 50, 51]
# branches []

import pytest
from hashlib import sha1, sha256
from ansible.utils.hashing import secure_hash_s
from ansible.module_utils._text import to_bytes

def test_secure_hash_s_sha1():
    data = "test data"
    expected_hash = sha1(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_sha256():
    data = "test data"
    expected_hash = sha256(to_bytes(data, errors='surrogate_or_strict')).hexdigest()
    assert secure_hash_s(data, hash_func=sha256) == expected_hash
