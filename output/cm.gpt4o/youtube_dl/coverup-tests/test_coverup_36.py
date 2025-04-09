# file youtube_dl/aes.py:289-290
# lines [290]
# branches []

import pytest
from youtube_dl.aes import rotate

def test_rotate():
    data = [1, 2, 3, 4]
    rotated_data = rotate(data)
    assert rotated_data == [2, 3, 4, 1], "The rotate function did not return the expected result"
