# file lib/ansible/utils/hashing.py:54-70
# lines [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# branches ['57->58', '57->59', '64->65', '64->67']

import os
import pytest
from hashlib import sha1
from ansible.utils.hashing import secure_hash
from ansible.errors import AnsibleError

def test_secure_hash_file_not_present(mocker):
    mocker.patch('os.path.exists', return_value=False)
    assert secure_hash('non_existent_file') is None

def test_secure_hash_is_directory(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    assert secure_hash('some_directory') is None

def test_secure_hash_io_error(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('builtins.open', side_effect=IOError("Permission denied"))
    
    with pytest.raises(AnsibleError) as excinfo:
        secure_hash('some_file')
    assert "error while accessing the file some_file, error was: Permission denied" in str(excinfo.value)

def test_secure_hash_success(mocker, tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("This is a test file.")

    # Calculate the expected hash
    expected_hash = sha1()
    expected_hash.update(b"This is a test file.")
    expected_hash_digest = expected_hash.hexdigest()

    # Test the secure_hash function
    assert secure_hash(str(test_file)) == expected_hash_digest
