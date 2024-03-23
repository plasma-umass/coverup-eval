# file pymonet/box.py:59-68
# lines [66, 68]
# branches []

import pytest
from pymonet.box import Box

def test_box_to_maybe():
    # Create a Box instance with a value
    box = Box(42)

    # Call to_maybe, which should trigger the import and usage of Maybe.just
    maybe = box.to_maybe()

    # Assert that the result is an instance of Maybe
    from pymonet.maybe import Maybe
    assert isinstance(maybe, Maybe)

    # Assert that the Maybe monad contains the correct value
    assert maybe.value == 42
