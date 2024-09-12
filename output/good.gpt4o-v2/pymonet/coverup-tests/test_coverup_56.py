# file: pymonet/maybe.py:127-138
# asked: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}
# gained: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_maybe_to_box_with_value():
    maybe = Maybe(42, is_nothing=False)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value == 42

def test_maybe_to_box_with_nothing():
    maybe = Maybe(None, is_nothing=True)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value is None
