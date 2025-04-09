# file lib/ansible/utils/hashing.py:95-98
# lines [98]
# branches ['96->98']

import pytest
import hashlib
from ansible.utils.hashing import md5

def test_md5_executes_secure_hash_when_md5_available(mocker, tmp_path):
    # Setup a temporary file to hash
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("content to hash")

    # Mock _md5 to be hashlib.md5 to ensure it is available
    mocker.patch('ansible.utils.hashing._md5', hashlib.md5)

    # Call the md5 function to hit line 98
    result = md5(str(test_file))

    # Verify that the result is a valid MD5 hash by comparing it to a known hash
    expected_hash = hashlib.md5()
    with open(str(test_file), 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            expected_hash.update(chunk)
    assert result == expected_hash.hexdigest()
