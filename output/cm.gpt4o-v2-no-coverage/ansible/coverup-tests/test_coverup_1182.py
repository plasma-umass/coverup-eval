# file: lib/ansible/utils/hashing.py:89-92
# asked: {"lines": [90, 91, 92], "branches": [[90, 91], [90, 92]]}
# gained: {"lines": [90, 91, 92], "branches": [[90, 91], [90, 92]]}

import pytest
from hashlib import md5 as _md5
from ansible.utils.hashing import md5s

def test_md5s_with_valid_data():
    data = "test data"
    expected_hash = _md5(data.encode()).hexdigest()
    assert md5s(data) == expected_hash

def test_md5s_md5_not_available(monkeypatch):
    def mock_md5():
        return None
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5s("test data")
