# file lib/ansible/cli/scripts/ansible_connection_cli_stub.py:53-65
# lines [61, 62, 63, 64, 65]
# branches []

import os
import pytest
import fcntl
from contextlib import contextmanager
from unittest.mock import patch

# Assuming the file_lock function is part of a module named ansible_connection_cli_stub
from ansible.cli.scripts.ansible_connection_cli_stub import file_lock

def test_file_lock():
    lock_path = 'test.lock'

    # Ensure the lock file is removed after the test
    try:
        with file_lock(lock_path):
            # Inside the context manager, the file should be locked
            assert os.path.exists(lock_path), "Lock file does not exist"

        # After the context manager, the lock should be released
        # Attempt to acquire the lock again to ensure it has been released
        with open(lock_path, 'r') as lock_file:
            fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            # If we reach this point, the lock was successfully acquired
            fcntl.flock(lock_file, fcntl.LOCK_UN)

    finally:
        # Clean up the lock file
        os.remove(lock_path)

# Mock os.open to raise an OSError to test exception handling
def test_file_lock_exception(mocker):
    lock_path = 'test.lock'
    mocker.patch('os.open', side_effect=OSError)

    with pytest.raises(OSError):
        with file_lock(lock_path):
            pass  # This block should not be executed due to the exception

    # Ensure the lock file is not created
    assert not os.path.exists(lock_path), "Lock file should not have been created"
