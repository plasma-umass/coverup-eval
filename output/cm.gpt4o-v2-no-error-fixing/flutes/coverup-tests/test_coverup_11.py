# file: flutes/iterator.py:343-344
# asked: {"lines": [343, 344], "branches": []}
# gained: {"lines": [343, 344], "branches": []}

import pytest
from flutes.iterator import Range

def test_get_idx():
    r = Range(1, 10, 2)
    assert r._get_idx(0) == 1
    assert r._get_idx(1) == 3
    assert r._get_idx(2) == 5
    assert r._get_idx(3) == 7
    assert r._get_idx(4) == 9
