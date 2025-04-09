# file: lib/ansible/module_utils/connection.py:47-67
# asked: {"lines": [47, 58, 62, 63, 65, 66, 67], "branches": []}
# gained: {"lines": [47, 58, 62, 63, 65, 66, 67], "branches": []}

import os
import hashlib
import pytest
from ansible.module_utils._text import to_bytes
from ansible.module_utils.six.moves import cPickle
from ansible.module_utils.connection import write_to_file_descriptor

def test_write_to_file_descriptor(monkeypatch):
    # Create a temporary file and get its file descriptor
    temp_file = os.open('temp_test_file', os.O_RDWR | os.O_CREAT)
    
    # Define a sample object to pickle and write
    sample_obj = {'key': 'value'}
    
    # Mock os.write to capture the writes
    writes = []
    def mock_write(fd, data):
        writes.append(data)
        return len(data)
    
    monkeypatch.setattr(os, 'write', mock_write)
    
    # Call the function
    write_to_file_descriptor(temp_file, sample_obj)
    
    # Verify the writes
    assert len(writes) == 3
    src = cPickle.dumps(sample_obj, protocol=0).replace(b'\r', br'\r')
    data_hash = to_bytes(hashlib.sha1(src).hexdigest())
    
    assert writes[0] == b'%d\n' % len(src)
    assert writes[1] == src
    assert writes[2] == b'%s\n' % data_hash
    
    # Clean up
    os.close(temp_file)
    os.remove('temp_test_file')
