# file: lib/ansible/utils/hashing.py:89-92
# asked: {"lines": [90, 91, 92], "branches": [[90, 91], [90, 92]]}
# gained: {"lines": [90, 91, 92], "branches": [[90, 91], [90, 92]]}

import pytest
from hashlib import md5 as _md5
from ansible.utils.hashing import md5s

def test_md5s_with_md5_available(monkeypatch):
    # Ensure _md5 is available
    monkeypatch.setattr('ansible.utils.hashing._md5', _md5)
    
    data = "test data"
    result = md5s(data)
    
    expected_result = _md5(data.encode()).hexdigest()
    assert result == expected_result

def test_md5s_without_md5(monkeypatch):
    # Simulate _md5 being None
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5s("test data")
