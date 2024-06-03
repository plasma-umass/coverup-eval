# file flutes/iterator.py:23-44
# lines [35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# branches ['35->36', '35->37', '38->39', '38->43', '40->38', '40->41', '43->exit', '43->44']

import pytest
from flutes.iterator import chunk

def test_chunk():
    # Test with n <= 0 to cover lines 35-36
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(0, range(10)))
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(-1, range(10)))

    # Test with n > 0 to cover lines 37-44
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

    result = list(chunk(4, range(10)))
    assert result == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

    result = list(chunk(1, range(3)))
    assert result == [[0], [1], [2]]

    result = list(chunk(5, range(0)))
    assert result == []

    result = list(chunk(2, [1, 2, 3, 4, 5]))
    assert result == [[1, 2], [3, 4], [5]]
