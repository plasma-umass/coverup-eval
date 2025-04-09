# file lib/ansible/utils/hashing.py:95-98
# lines [95, 96, 97, 98]
# branches ['96->97', '96->98']

import pytest
from unittest import mock
from ansible.utils.hashing import md5

def test_md5_fips_mode(mocker):
    # Mock the _md5 variable to simulate FIPS mode
    mocker.patch('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5('dummy_filename')

def test_md5_success(mocker):
    # Mock the _md5 variable to simulate MD5 being available
    mock_md5 = mock.Mock()
    mocker.patch('ansible.utils.hashing._md5', mock_md5)
    
    # Mock the secure_hash function to avoid actual file operations
    mock_secure_hash = mocker.patch('ansible.utils.hashing.secure_hash', return_value='dummy_hash')
    
    result = md5('dummy_filename')
    
    mock_secure_hash.assert_called_once_with('dummy_filename', mock_md5)
    assert result == 'dummy_hash'
