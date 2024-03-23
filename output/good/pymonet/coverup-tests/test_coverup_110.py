# file pymonet/box.py:48-57
# lines [48, 57]
# branches []

import pytest
from pymonet.box import Box

def test_box_ap():
    box_value = Box(10)
    box_function = Box(lambda x: x * 2)

    result = box_function.ap(box_value)
    assert result.value == 20

def test_box_ap_with_callable_containing_non_callable():
    with pytest.raises(TypeError):
        box_value = Box(10)
        box_non_callable = Box(lambda x: x)  # This should be a function, but it's not callable with an int
        box_value.ap(box_non_callable)  # This should raise a TypeError
