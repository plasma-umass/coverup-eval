# file: lib/ansible/utils/hashing.py:89-92
# asked: {"lines": [89, 90, 91, 92], "branches": [[90, 91], [90, 92]]}
# gained: {"lines": [89, 90, 91, 92], "branches": [[90, 91], [90, 92]]}

import pytest
from unittest import mock

# Assuming _md5 and secure_hash_s are defined in the module ansible.utils.hashing
from ansible.utils.hashing import md5s

def test_md5s_md5_not_available(monkeypatch):
    # Mock _md5 to be None
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5s(b'test data')

def test_md5s_md5_available(monkeypatch):
    # Mock _md5 and secure_hash_s
    mock_md5 = mock.Mock()
    mock_secure_hash_s = mock.Mock(return_value='mocked_hash')
    
    monkeypatch.setattr('ansible.utils.hashing._md5', mock_md5)
    monkeypatch.setattr('ansible.utils.hashing.secure_hash_s', mock_secure_hash_s)
    
    result = md5s(b'test data')
    
    mock_secure_hash_s.assert_called_once_with(b'test data', mock_md5)
    assert result == 'mocked_hash'
