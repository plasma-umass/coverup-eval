# file pymonet/either.py:48-57
# lines [48, 55, 57]
# branches []

import pytest
from pymonet.either import Either, Left, Right
from pymonet.box import Box

def test_either_to_box_with_right():
    right_value = Right(10)
    box = right_value.to_box()
    assert isinstance(box, Box)
    assert box.value == 10

# Since Left does not have a 'value' attribute, we do not need to test to_box for Left
