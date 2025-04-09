# file: sty/primitive.py:181-193
# asked: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [181, 185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

import pytest
from sty.primitive import Register

def test_as_dict():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.test_attr1 = "value1"
            self.test_attr2 = "value2"
            self._private_attr = "should_not_include"

    reg = TestRegister()
    result = reg.as_dict()

    assert result == {
        "test_attr1": "value1",
        "test_attr2": "value2"
    }
