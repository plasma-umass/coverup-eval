# file: lib/ansible/utils/hashing.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}
# gained: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}

import pytest
import hashlib
from unittest.mock import patch

# Assuming _md5 and secure_hash are defined in ansible.utils.hashing
from ansible.utils.hashing import md5

def test_md5_no_md5_available(monkeypatch):
    def mock_md5():
        return None

    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5('dummy_filename')

def test_md5_with_md5_available(monkeypatch):
    mock_md5 = hashlib.md5

    def mock_secure_hash(filename, hash_func):
        assert filename == 'dummy_filename'
        assert hash_func == mock_md5
        return 'mocked_hash'

    monkeypatch.setattr('ansible.utils.hashing._md5', mock_md5)
    monkeypatch.setattr('ansible.utils.hashing.secure_hash', mock_secure_hash)
    result = md5('dummy_filename')
    assert result == 'mocked_hash'
