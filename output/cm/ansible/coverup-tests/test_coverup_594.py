# file lib/ansible/utils/hashing.py:95-98
# lines [95, 96, 97, 98]
# branches ['96->97', '96->98']

import pytest
from ansible.utils.hashing import md5
from unittest.mock import patch

# Test function to cover the missing branch where _md5 is not available
def test_md5_not_available(tmp_path, mocker):
    # Create a temporary file to use for testing
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("content")

    # Mock the _md5 to be None to simulate the environment where MD5 is not available
    mocker.patch('ansible.utils.hashing._md5', None)

    # Assert that the correct exception is raised when MD5 is not available
    with pytest.raises(ValueError) as excinfo:
        md5(str(test_file))
    assert 'MD5 not available.  Possibly running in FIPS mode' in str(excinfo.value)
