# file youtube_dl/aes.py:289-290
# lines [290]
# branches []

import pytest
from youtube_dl.aes import rotate

def test_rotate():
    # Test with non-empty list
    data = [1, 2, 3, 4]
    expected = [2, 3, 4, 1]
    assert rotate(data) == expected, "rotate should move the first element to the end"

    # Test with single element list
    data_single = [1]
    expected_single = [1]
    assert rotate(data_single) == expected_single, "rotate should handle single element list without change"

    # Test with empty list should be skipped as the function does not handle empty lists
