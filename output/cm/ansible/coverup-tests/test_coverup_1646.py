# file lib/ansible/module_utils/connection.py:47-67
# lines [58, 62, 63, 65, 66, 67]
# branches []

import hashlib
import os
import pytest
from ansible.module_utils.connection import write_to_file_descriptor
from io import BytesIO
import pickle as cPickle

def test_write_to_file_descriptor(mocker):
    # Mock os.write to capture its calls
    write_calls = []

    def mock_write(fd, data):
        write_calls.append(data)
        return len(data)

    mocker.patch('os.write', side_effect=mock_write)

    # Create a test object to be pickled
    test_obj = {'key': 'value'}

    # Use a BytesIO object as a file descriptor to avoid actual file operations
    fake_fd = BytesIO()

    # Call the function under test
    write_to_file_descriptor(fake_fd, test_obj)

    # Verify that os.write was called with the expected data
    assert len(write_calls) == 3, "os.write should be called exactly 3 times"

    # Unpickle the data to verify it matches the original object
    pickled_data = write_calls[1]
    unpickled_obj = cPickle.loads(pickled_data)
    assert unpickled_obj == test_obj, "The pickled and then unpickled object should match the original"

    # Verify the length and hash were written correctly
    expected_length = len(pickled_data)
    expected_hash = hashlib.sha1(pickled_data).hexdigest().encode()
    assert write_calls[0] == b'%d\n' % expected_length, "The first write should be the length of the pickled data"
    assert write_calls[2].strip() == expected_hash, "The third write should be the SHA1 hash of the pickled data"

    # Clean up the BytesIO object
    fake_fd.close()
