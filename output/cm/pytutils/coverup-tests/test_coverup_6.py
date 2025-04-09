# file pytutils/path.py:4-6
# lines [4, 5, 6]
# branches ['5->exit', '5->6']

import os
import pytest
from pytutils.path import join_each

def test_join_each(tmp_path):
    # Create a temporary directory and a list of filenames
    parent = tmp_path / "parent"
    parent.mkdir()
    filenames = ["file1.txt", "file2.txt", "file3.txt"]

    # Use the join_each function to join the parent path with each filename
    joined_paths = list(join_each(str(parent), filenames))

    # Check if the joined paths are correct
    for filename, joined_path in zip(filenames, joined_paths):
        assert joined_path == os.path.join(str(parent), filename)

    # No cleanup required as tmp_path is a pytest fixture that handles cleanup
