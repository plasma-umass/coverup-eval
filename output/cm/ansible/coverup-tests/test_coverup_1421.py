# file lib/ansible/utils/hashing.py:89-92
# lines [92]
# branches ['90->92']

import pytest
from ansible.utils.hashing import md5s
from hashlib import md5

def test_md5s_with_available_md5(mocker):
    # Mock the _md5 function to return the hashlib md5 function
    mocker.patch('ansible.utils.hashing._md5', new=md5)

    # Test that the md5s function returns the correct MD5 hash
    test_data = b"test data"
    expected_hash = md5(test_data).hexdigest()
    result_hash = md5s(test_data)

    # Assert that the result is the expected hash
    assert result_hash == expected_hash

    # Clean up the mock
    mocker.stopall()
