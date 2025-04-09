# file flutes/iterator.py:330-331
# lines [330, 331]
# branches []

import pytest
from flutes.iterator import Range

def test_range_iterator():
    r = Range(0, 5, 1)
    iterator = iter(r)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    with pytest.raises(StopIteration):
        next(iterator)
