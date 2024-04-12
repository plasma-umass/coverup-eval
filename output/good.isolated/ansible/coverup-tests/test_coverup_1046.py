# file lib/ansible/parsing/dataloader.py:34-52
# lines [34, 36]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound
import os
import tempfile

# Test function to cover missing lines/branches in DataLoader
def test_dataloader_load_from_nonexistent_file(mocker):
    # Setup
    dl = DataLoader()
    fake_file = '/path/to/nonexistent/file'

    # Mock the os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)

    # Execute and assert that AnsibleFileNotFound is raised
    with pytest.raises(AnsibleFileNotFound):
        dl.load_from_file(fake_file)

    # Cleanup is not necessary as we are mocking os.path.exists and no file is created
