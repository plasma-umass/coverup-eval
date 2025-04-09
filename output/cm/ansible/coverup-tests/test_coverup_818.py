# file lib/ansible/parsing/dataloader.py:120-122
# lines [120, 121, 122]
# branches []

import os
import pytest
from ansible.parsing.dataloader import DataLoader

# Assuming the DataLoader class is part of a larger module, we'll need to mock out
# any dependencies not relevant to the test, such as `self.path_dwim`.

def test_list_directory(mocker, tmp_path):
    # Create a temporary directory and files for the test
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("content1")
    (test_dir / "file2.txt").write_text("content2")

    # Mock the path_dwim method to return the actual filesystem path
    mocker.patch.object(DataLoader, 'path_dwim', return_value=str(test_dir))

    # Instantiate DataLoader and call the method under test
    data_loader = DataLoader()
    files = data_loader.list_directory(test_dir)

    # Verify the list_directory method returns the correct file list
    assert sorted(files) == ['file1.txt', 'file2.txt']

    # No cleanup needed as pytest handles the temporary directory
