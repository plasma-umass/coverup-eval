# file: lib/ansible/utils/hashing.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}
# gained: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}

import pytest
from ansible.utils.hashing import md5, secure_hash

def test_md5_fips_mode(monkeypatch):
    # Simulate FIPS mode by setting _md5 to None
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5('dummy_filename')

def test_md5_success(monkeypatch, mocker):
    # Mock _md5 to simulate normal operation
    mock_md5 = mocker.Mock()
    monkeypatch.setattr('ansible.utils.hashing._md5', mock_md5)
    
    # Mock secure_hash to avoid actual file operations
    mock_secure_hash = mocker.patch('ansible.utils.hashing.secure_hash', return_value='mocked_hash')
    
    result = md5('dummy_filename')
    
    mock_secure_hash.assert_called_once_with('dummy_filename', mock_md5)
    assert result == 'mocked_hash'
