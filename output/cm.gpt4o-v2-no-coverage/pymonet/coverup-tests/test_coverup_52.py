# file: pymonet/maybe.py:127-138
# asked: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}
# gained: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

class TestMaybe:
    def test_to_box_with_value(self):
        just = Maybe(42, False)
        box = just.to_box()
        assert isinstance(box, Box)
        assert box.value == 42

    def test_to_box_with_nothing(self):
        nothing = Maybe(None, True)
        box = nothing.to_box()
        assert isinstance(box, Box)
        assert box.value is None
