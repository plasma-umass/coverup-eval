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
    # Create a mock for os.write
    mock_write = mocker.patch('os.write')

    # Create a pipe to get a file descriptor
    r_fd, w_fd = os.pipe()

    try:
        # Test object to write
        test_obj = {'key': 'value'}

        # Call the function
        write_to_file_descriptor(w_fd, test_obj)

        # Verify the calls to os.write
        src = cPickle.dumps(test_obj, protocol=0)
        src = src.replace(b'\r', b'\\r')
        data_hash = to_bytes(hashlib.sha1(src).hexdigest())

        expected_calls = [
            mocker.call(w_fd, b'%d\n' % len(src)),
            mocker.call(w_fd, src),
            mocker.call(w_fd, b'%s\n' % data_hash)
        ]

        mock_write.assert_has_calls(expected_calls, any_order=False)

    finally:
        # Close the file descriptors
        os.close(r_fd)
        os.close(w_fd)
