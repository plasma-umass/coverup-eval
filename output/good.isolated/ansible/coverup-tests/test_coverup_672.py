# file lib/ansible/utils/hashing.py:45-51
# lines [45, 48, 49, 50, 51]
# branches []

import pytest
from ansible.utils.hashing import secure_hash_s
from hashlib import sha1, sha256

def test_secure_hash_s_sha256():
    test_data = "ansible_test_data"
    expected_sha256_hexdigest = sha256(test_data.encode('utf-8')).hexdigest()

    # Test with sha256 hash function
    result = secure_hash_s(test_data, hash_func=sha256)
    assert result == expected_sha256_hexdigest, "SHA256 hexdigest does not match expected value"

def test_secure_hash_s_default_sha1():
    test_data = "ansible_test_data"
    expected_sha1_hexdigest = sha1(test_data.encode('utf-8')).hexdigest()

    # Test with default hash function (sha1)
    result = secure_hash_s(test_data)
    assert result == expected_sha1_hexdigest, "SHA1 hexdigest does not match expected value"
