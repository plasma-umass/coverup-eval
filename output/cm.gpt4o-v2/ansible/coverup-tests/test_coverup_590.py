# file: lib/ansible/utils/hashing.py:89-92
# asked: {"lines": [89, 90, 91, 92], "branches": [[90, 91], [90, 92]]}
# gained: {"lines": [89, 90, 91, 92], "branches": [[90, 91], [90, 92]]}

import pytest
from hashlib import md5 as _md5
from ansible.utils.hashing import md5s

def test_md5s_with_md5_available(monkeypatch):
    def mock_md5():
        return _md5()
    
    monkeypatch.setattr('ansible.utils.hashing._md5', mock_md5)
    
    data = "test data"
    result = md5s(data)
    assert result == _md5(data.encode()).hexdigest()

def test_md5s_without_md5(monkeypatch):
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5s("test data")
