# file lib/ansible/utils/hashing.py:54-70
# lines [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# branches ['57->58', '57->59', '64->65', '64->67']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.utils.hashing import secure_hash
from hashlib import sha1

def test_secure_hash_file_not_exists(mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('os.path.isdir', return_value=False)
    assert secure_hash('nonexistentfile') is None

def test_secure_hash_file_is_directory(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    assert secure_hash('directory') is None

def test_secure_hash_io_error(mocker, tmp_path):
    # Create a temporary file and then delete it to provoke an IOError
    temp_file = tmp_path / "tempfile"
    temp_file.write_text("content")
    file_path = str(temp_file)
    temp_file.unlink()

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    with pytest.raises(AnsibleError) as excinfo:
        secure_hash(file_path)
    assert "error while accessing the file" in str(excinfo.value)

def test_secure_hash_success(tmp_path):
    # Create a temporary file with known content
    temp_file = tmp_path / "tempfile"
    temp_file.write_text("content")
    expected_hash = sha1(b"content").hexdigest()

    # Test that the hash matches the expected hash
    assert secure_hash(str(temp_file)) == expected_hash
