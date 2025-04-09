# file: tqdm/auto.py:38-42
# asked: {"lines": [42], "branches": []}
# gained: {"lines": [42], "branches": []}

import pytest
from tqdm.auto import trange

def test_trange():
    # Test with a simple range
    t = trange(5)
    assert list(t) == [0, 1, 2, 3, 4]
    t.close()

    # Test with a range and additional arguments
    t = trange(1, 5, 2)
    assert list(t) == [1, 3]
    t.close()

    # Test with a range and keyword arguments
    t = trange(5, desc="Test")
    assert list(t) == [0, 1, 2, 3, 4]
    t.close()
