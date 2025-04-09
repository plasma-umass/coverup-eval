# file: lib/ansible/utils/hashing.py:45-51
# asked: {"lines": [45, 48, 49, 50, 51], "branches": []}
# gained: {"lines": [45, 48, 49, 50, 51], "branches": []}

import pytest
from hashlib import sha1, sha256
from ansible.utils.hashing import secure_hash_s

def test_secure_hash_s_sha1():
    data = "test data"
    expected_hash = sha1(data.encode('utf-8')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_sha256():
    data = "test data"
    expected_hash = sha256(data.encode('utf-8')).hexdigest()
    assert secure_hash_s(data, hash_func=sha256) == expected_hash

def test_secure_hash_s_empty_string():
    data = ""
    expected_hash = sha1(data.encode('utf-8')).hexdigest()
    assert secure_hash_s(data) == expected_hash

def test_secure_hash_s_non_ascii():
    data = "tęst dâtâ"
    expected_hash = sha1(data.encode('utf-8')).hexdigest()
    assert secure_hash_s(data) == expected_hash
