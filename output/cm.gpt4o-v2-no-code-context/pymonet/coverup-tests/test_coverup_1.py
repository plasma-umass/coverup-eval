# file: pymonet/maybe.py:127-138
# asked: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}
# gained: {"lines": [127, 134, 136, 137, 138], "branches": [[136, 137], [136, 138]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_maybe_to_box_with_value():
    maybe = Maybe.just(10)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value == 10

def test_maybe_to_box_with_nothing():
    maybe = Maybe.nothing()
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value is None
