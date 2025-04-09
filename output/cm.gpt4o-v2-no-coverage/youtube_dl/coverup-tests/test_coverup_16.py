# file: youtube_dl/aes.py:289-290
# asked: {"lines": [290], "branches": []}
# gained: {"lines": [290], "branches": []}

import pytest
from youtube_dl.aes import rotate

def test_rotate():
    data = [1, 2, 3, 4]
    expected_result = [2, 3, 4, 1]
    result = rotate(data)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    data = ['a', 'b', 'c']
    expected_result = ['b', 'c', 'a']
    result = rotate(data)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    data = [1]
    expected_result = [1]
    result = rotate(data)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    data = []
    with pytest.raises(IndexError):
        rotate(data)
