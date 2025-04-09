# file: lib/ansible/utils/hashing.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}
# gained: {"lines": [95, 96, 97, 98], "branches": [[96, 97], [96, 98]]}

import pytest
import os
from ansible.errors import AnsibleError
from ansible.utils.hashing import md5, secure_hash

def test_md5_with_md5_available(monkeypatch, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "testfile.txt"
    temp_file.write_text("This is a test file.")

    # Ensure _md5 is available
    from hashlib import md5 as _md5
    monkeypatch.setattr('ansible.utils.hashing._md5', _md5)

    # Call the md5 function and check the result
    result = md5(str(temp_file))
    assert result == secure_hash(str(temp_file), _md5)

def test_md5_with_md5_unavailable(monkeypatch):
    # Ensure _md5 is not available
    monkeypatch.setattr('ansible.utils.hashing._md5', None)

    # Call the md5 function and check for ValueError
    with pytest.raises(ValueError, match='MD5 not available.  Possibly running in FIPS mode'):
        md5("dummy_filename")

def test_secure_hash_file_not_present():
    # Call secure_hash with a non-existent file
    result = secure_hash("non_existent_file.txt")
    assert result is None

def test_secure_hash_is_directory(tmp_path):
    # Call secure_hash with a directory
    result = secure_hash(str(tmp_path))
    assert result is None

def test_secure_hash_io_error(monkeypatch, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "testfile.txt"
    temp_file.write_text("This is a test file.")

    # Simulate IOError
    def mock_open(*args, **kwargs):
        raise IOError("Mocked IOError")

    monkeypatch.setattr("builtins.open", mock_open)

    # Call secure_hash and check for AnsibleError
    with pytest.raises(AnsibleError, match='error while accessing the file'):
        secure_hash(str(temp_file))
