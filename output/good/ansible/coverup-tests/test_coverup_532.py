# file lib/ansible/playbook/included_file.py:39-45
# lines [39, 40, 41, 42, 43, 44, 45]
# branches []

import pytest
from ansible.playbook.included_file import IncludedFile

# Assuming the IncludedFile class is the only class in the included_file.py file
# and that the file structure provided in the question is accurate.

@pytest.fixture
def cleanup_hosts():
    # Fixture to cleanup after test
    yield
    # No specific cleanup needed as the test does not modify external state

def test_included_file_initialization(cleanup_hosts):
    # Setup
    filename = "test_file.yml"
    args = {"some_arg": "value"}
    vars = {"some_var": "value"}
    task = "test_task"
    is_role = True

    # Exercise
    included_file = IncludedFile(filename, args, vars, task, is_role)

    # Verify
    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_file._task == task
    assert included_file._hosts == []
    assert included_file._is_role == is_role

    # Cleanup is handled by the cleanup_hosts fixture
