# file sty/primitive.py:181-193
# lines [181, 185, 187, 189, 191, 193]
# branches ['187->189', '187->193', '189->187', '189->191']

import pytest
from sty.primitive import Register

def test_register_as_dict():
    class TestRegister(Register):
        color1 = "red"
        color2 = "blue"
        _private_color = "green"
        number = 123

    reg = TestRegister()
    result = reg.as_dict()
    
    assert result == {"color1": "red", "color2": "blue"}
    assert "_private_color" not in result
    assert "number" not in result
