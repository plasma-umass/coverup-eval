# file lib/ansible/utils/hashing.py:89-92
# lines [89, 90, 91, 92]
# branches ['90->91', '90->92']

import pytest
from unittest import mock

# Import the module and function
from ansible.utils.hashing import md5s

def test_md5s_no_md5(mocker):
    # Mock the _md5 variable to be None
    mocker.patch('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5s(b'test data')

def test_md5s_with_md5(mocker):
    # Mock the _md5 variable to be a valid hash function
    mock_md5 = mock.Mock()
    mocker.patch('ansible.utils.hashing._md5', mock_md5)
    
    # Mock the secure_hash_s function to return a specific value
    mock_secure_hash_s = mocker.patch('ansible.utils.hashing.secure_hash_s', return_value='mocked_hash')
    
    result = md5s(b'test data')
    
    # Assert that secure_hash_s was called with the correct parameters
    mock_secure_hash_s.assert_called_once_with(b'test data', mock_md5)
    
    # Assert that the result is as expected
    assert result == 'mocked_hash'
