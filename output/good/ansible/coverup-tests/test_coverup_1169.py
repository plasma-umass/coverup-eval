# file lib/ansible/module_utils/facts/utils.py:23-60
# lines [33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 46, 48, 49, 51, 52, 54, 56, 58, 60]
# branches ['34->35', '34->60', '48->49', '48->51', '51->52', '51->58']

import os
import pytest
import tempfile
import fcntl

from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content(mocker):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name
        tmp.write(b"Test content\n")
        tmp.flush()
        os.fsync(tmp.fileno())

    # Mock os.access to return True
    mocker.patch('os.access', return_value=True)

    # Mock fcntl to raise an exception to cover lines 42-43
    mocker.patch('fcntl.fcntl', side_effect=Exception())

    # Read the content to cover lines 33-60
    content = get_file_content(tmp_path, default="default", strip=True)

    # Assert the content is correct and stripped
    assert content == "Test content"

    # Clean up the temporary file
    os.unlink(tmp_path)
