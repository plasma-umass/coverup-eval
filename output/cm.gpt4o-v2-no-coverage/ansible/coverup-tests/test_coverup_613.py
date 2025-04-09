# file: lib/ansible/module_utils/connection.py:47-67
# asked: {"lines": [47, 58, 62, 63, 65, 66, 67], "branches": []}
# gained: {"lines": [47, 58, 62, 63, 65, 66, 67], "branches": []}

import os
import hashlib
import pytest
from ansible.module_utils._text import to_bytes
from ansible.module_utils.six.moves import cPickle
from ansible.module_utils.connection import write_to_file_descriptor

def test_write_to_file_descriptor(mocker):
    # Mock os.write to avoid actual file descriptor operations
    mock_write = mocker.patch('os.write')

    # Create a sample object to serialize
    sample_obj = {'key': 'value'}

    # Create a mock file descriptor
    mock_fd = 1

    # Call the function
    write_to_file_descriptor(mock_fd, sample_obj)

    # Verify that os.write was called with the correct parameters
    src = cPickle.dumps(sample_obj, protocol=0)
    src = src.replace(b'\r', br'\r')
    data_hash = to_bytes(hashlib.sha1(src).hexdigest())

    expected_calls = [
        mocker.call(mock_fd, b'%d\n' % len(src)),
        mocker.call(mock_fd, src),
        mocker.call(mock_fd, b'%s\n' % data_hash)
    ]

    mock_write.assert_has_calls(expected_calls)
