# file flutes/iterator.py:69-89
# lines [69, 81, 82, 83, 84, 85, 86, 87, 88, 89]
# branches ['81->82', '81->83', '85->86', '85->87']

import pytest
from flutes.iterator import drop

def test_drop():
    # Test dropping elements from a list
    result = list(drop(3, [1, 2, 3, 4, 5]))
    assert result == [4, 5]

    # Test dropping more elements than present in the list
    result = list(drop(10, [1, 2, 3]))
    assert result == []

    # Test dropping zero elements
    result = list(drop(0, [1, 2, 3]))
    assert result == [1, 2, 3]

    # Test dropping elements from an empty list
    result = list(drop(3, []))
    assert result == []

    # Test dropping elements from a generator
    result = list(drop(2, (x for x in range(5))))
    assert result == [2, 3, 4]

    # Test dropping elements from a string
    result = list(drop(2, "hello"))
    assert result == ['l', 'l', 'o']

    # Test dropping elements from a tuple
    result = list(drop(2, (1, 2, 3, 4)))
    assert result == [3, 4]

    # Test dropping elements from a set (order is not guaranteed)
    result = sorted(drop(2, {1, 2, 3, 4}))
    assert result == [3, 4]

    # Test dropping elements with n being negative
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(drop(-1, [1, 2, 3]))

    # Test StopIteration handling
    result = list(drop(5, [1, 2, 3]))
    assert result == []

