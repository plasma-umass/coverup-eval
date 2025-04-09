# file: lib/ansible/utils/hashing.py:54-70
# asked: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}
# gained: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}

import os
import pytest
from hashlib import sha1
from ansible.errors import AnsibleError
from ansible.utils.hashing import secure_hash

def test_secure_hash_file_not_exists(monkeypatch):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert secure_hash('non_existent_file') is None

def test_secure_hash_is_directory(monkeypatch):
    def mock_exists(path):
        return True

    def mock_isdir(path):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    assert secure_hash('some_directory') is None

def test_secure_hash_file_read_error(monkeypatch):
    def mock_exists(path):
        return True

    def mock_isdir(path):
        return False

    def mock_open(*args, **kwargs):
        raise IOError("mocked error")

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr('builtins.open', mock_open)
    
    with pytest.raises(AnsibleError, match="error while accessing the file some_file, error was: mocked error"):
        secure_hash('some_file')

def test_secure_hash_success(monkeypatch, tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("test content")

    def mock_exists(path):
        return True

    def mock_isdir(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)

    expected_hash = sha1(b"test content").hexdigest()
    assert secure_hash(str(test_file)) == expected_hash
