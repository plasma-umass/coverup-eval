# file: flutes/iterator.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_iter():
    r = Range(1, 10, 2)
    it = iter(r)
    assert isinstance(it, Range)
    assert list(it) == [1, 3, 5, 7, 9]
