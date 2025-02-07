# file: sty/primitive.py:181-193
# asked: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

import pytest
from sty.primitive import Register

def test_as_dict():
    class TestRegister(Register):
        def __init__(self):
            self.color1 = "red"
            self.color2 = "blue"
            self._private = "should not be included"
            self.number = 123  # should not be included as it's not a string

    reg = TestRegister()
    result = reg.as_dict()
    
    assert result == {"color1": "red", "color2": "blue"}

    # Clean up
    del TestRegister
    del reg
    del result
