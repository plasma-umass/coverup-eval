# file flutes/iterator.py:253-256
# lines [253, 254, 255, 256]
# branches []

import pytest
from flutes.iterator import LazyList

def test_lazy_list():
    # Create a simple generator function
    def simple_gen():
        yield from range(3)

    # Instantiate LazyList with the generator
    lazy_list = LazyList(simple_gen())

    # Access elements to ensure the generator is being consumed
    assert lazy_list[0] == 0
    assert lazy_list[1] == 1
    assert lazy_list[2] == 2

    # Check that the list is now exhausted
    with pytest.raises(IndexError):
        _ = lazy_list[3]

    # Ensure that the internal list has been populated
    assert lazy_list.list == [0, 1, 2]
    assert lazy_list.exhausted is True

    # Test that accessing an index within the range does not raise an error
    assert lazy_list[1] == 1
