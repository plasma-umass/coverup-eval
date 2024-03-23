# file lib/ansible/plugins/filter/core.py:108-110
# lines [108, 110]
# branches []

import os
import pytest
from ansible.plugins.filter.core import fileglob

# Test function for fileglob
def test_fileglob(tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    file1 = test_dir / "file1.txt"
    file1.touch()
    file2 = test_dir / "file2.txt"
    file2.touch()
    subdir = test_dir / "subdir"
    subdir.mkdir()
    subfile = subdir / "file3.txt"
    subfile.touch()

    # Test fileglob with a pattern that matches files only in the test_dir
    pattern = str(test_dir / "*.txt")
    matched_files = fileglob(pattern)

    # Assert that the returned list contains the correct files
    assert sorted(matched_files) == sorted([str(file1), str(file2)])

    # Clean up is handled by pytest using the tmp_path fixture
