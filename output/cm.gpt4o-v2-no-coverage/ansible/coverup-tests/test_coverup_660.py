# file: lib/ansible/utils/hashing.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}
# gained: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}

import pytest
from hashlib import md5 as _md5
from ansible.errors import AnsibleError
from ansible.utils.hashing import md5
from ansible.utils.hashing import secure_hash
import os

def test_md5(monkeypatch):
    # Test when _md5 is not available
    monkeypatch.setattr('ansible.utils.hashing._md5', None)
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5('dummyfile')

    # Restore _md5 for further tests
    monkeypatch.setattr('ansible.utils.hashing._md5', _md5)

    # Test when file does not exist
    monkeypatch.setattr('os.path.exists', lambda x: False)
    assert md5('dummyfile') is None

    # Test when file is a directory
    monkeypatch.setattr('os.path.exists', lambda x: True)
    monkeypatch.setattr('os.path.isdir', lambda x: True)
    assert md5('dummyfile') is None

    # Test when file is present and is not a directory
    test_content = b"test content"
    test_filename = 'testfile'
    with open(test_filename, 'wb') as f:
        f.write(test_content)

    monkeypatch.setattr('os.path.exists', lambda x: True)
    monkeypatch.setattr('os.path.isdir', lambda x: False)
    expected_md5 = _md5(test_content).hexdigest()
    assert md5(test_filename) == expected_md5

    os.remove(test_filename)

    # Test IOError handling
    def mock_open(*args, **kwargs):
        raise IOError("mocked error")
    monkeypatch.setattr('builtins.open', mock_open)
    with pytest.raises(AnsibleError, match='error while accessing the file dummyfile, error was: mocked error'):
        md5('dummyfile')
