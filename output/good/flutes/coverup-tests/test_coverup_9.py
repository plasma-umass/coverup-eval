# file flutes/iterator.py:23-44
# lines [23, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# branches ['35->36', '35->37', '38->39', '38->43', '40->38', '40->41', '43->exit', '43->44']

import pytest
from flutes.iterator import chunk

def test_chunk():
    # Test normal behavior
    chunks = list(chunk(3, range(10)))
    assert chunks == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

    # Test empty iterable
    empty_chunks = list(chunk(3, []))
    assert empty_chunks == []

    # Test chunk size larger than iterable
    large_chunk = list(chunk(15, range(10)))
    assert large_chunk == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

    # Test chunk size of 1
    single_chunks = list(chunk(1, range(3)))
    assert single_chunks == [[0], [1], [2]]

    # Test chunk size of 0 (should raise ValueError)
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))

    # Test chunk size of -1 (should raise ValueError)
    with pytest.raises(ValueError):
        list(chunk(-1, range(10)))

# No top-level code is included, as requested.
