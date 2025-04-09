# file: pymonet/box.py:48-57
# asked: {"lines": [57], "branches": []}
# gained: {"lines": [57], "branches": []}

import pytest
from pymonet.box import Box

class TestBox:
    def test_ap_with_function(self):
        box = Box(lambda x: x + 1)
        applicative = Box(2)
        result = box.ap(applicative)
        assert result.value == 3

    def test_ap_with_non_function(self):
        box = Box(5)
        applicative = Box(2)
        with pytest.raises(TypeError):
            box.ap(applicative)
