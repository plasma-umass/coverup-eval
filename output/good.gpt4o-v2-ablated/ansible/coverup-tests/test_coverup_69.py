# file: lib/ansible/utils/hashing.py:54-70
# asked: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}
# gained: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}

import os
import pytest
from hashlib import sha1
from ansible.errors import AnsibleError
from ansible.utils.hashing import secure_hash

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "testfile.txt"
    file.write_text("This is a test file.")
    return file

def test_secure_hash_file_not_exists():
    assert secure_hash("non_existent_file.txt") is None

def test_secure_hash_is_directory(tmp_path):
    assert secure_hash(tmp_path) is None

def test_secure_hash_success(temp_file):
    expected_hash = sha1()
    expected_hash.update(b"This is a test file.")
    assert secure_hash(temp_file) == expected_hash.hexdigest()

def test_secure_hash_io_error(monkeypatch, temp_file):
    def mock_open(*args, **kwargs):
        raise IOError("mocked IO error")
    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(AnsibleError, match="error while accessing the file"):
        secure_hash(temp_file)
