# file pytutils/path.py:4-6
# lines [4, 5, 6]
# branches ['5->exit', '5->6']

import os
import pytest
from pytutils.path import join_each

def test_join_each(mocker):
    # Mock os.path.join to ensure it is called correctly
    mock_join = mocker.patch('os.path.join', side_effect=lambda parent, p: f"{parent}/{p}")

    parent = "parent_dir"
    iterable = ["file1.txt", "file2.txt", "file3.txt"]
    expected = [f"{parent}/{p}" for p in iterable]

    result = list(join_each(parent, iterable))

    assert result == expected
    assert mock_join.call_count == len(iterable)
    for i, p in enumerate(iterable):
        mock_join.assert_any_call(parent, p)
