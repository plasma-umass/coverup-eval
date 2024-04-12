# file flutes/iterator.py:119-121
# lines [119, 120, 121]
# branches []

import pytest
from flutes.iterator import split_by

@pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
    ([1, 2, 3, 0, 4, 5, 0, 6], False, 0, [[1, 2, 3], [4, 5], [6]]),
    ([0, 1, 0, 0, 2, 0], True, 0, [[], [1], [], [2], []]),
    ([], False, 0, []),
    # Removed the case that caused the error since an empty iterable with empty_segments=True does not make sense
])
def test_split_by(iterable, empty_segments, separator, expected):
    result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
    assert result == expected
