# file: lib/ansible/utils/hashing.py:54-70
# asked: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}
# gained: {"lines": [54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[57, 58], [57, 59], [64, 65], [64, 67]]}

import os
import pytest
from hashlib import sha1
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes
from ansible.utils.hashing import secure_hash

def test_secure_hash_file_not_exists(mocker):
    mocker.patch('os.path.exists', return_value=False)
    result = secure_hash('non_existent_file.txt')
    assert result is None

def test_secure_hash_is_directory(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    result = secure_hash('some_directory')
    assert result is None

def test_secure_hash_io_error(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('builtins.open', side_effect=IOError('Permission denied'))
    
    with pytest.raises(AnsibleError) as excinfo:
        secure_hash('file_with_no_permission.txt')
    assert 'error while accessing the file file_with_no_permission.txt, error was: Permission denied' in str(excinfo.value)

def test_secure_hash_success(mocker, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("This is a test file.")

    result = secure_hash(str(temp_file))
    expected_hash = sha1()
    expected_hash.update(b"This is a test file.")
    
    assert result == expected_hash.hexdigest()
