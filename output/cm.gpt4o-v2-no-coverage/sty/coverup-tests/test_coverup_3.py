# file: sty/primitive.py:181-193
# asked: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

import pytest
from sty.primitive import Register

class TestRegister:
    def test_as_dict(self):
        # Create a mock Register object with some attributes
        class MockRegister(Register):
            color1 = "red"
            color2 = "blue"
            _private = "should not be included"
            number = 123  # should not be included

        reg = MockRegister()
        result = reg.as_dict()

        # Verify the result
        assert result == {"color1": "red", "color2": "blue"}

        # Ensure no private or non-string attributes are included
        assert "_private" not in result
        assert "number" not in result
