# file: pymonet/maybe.py:44-58
# asked: {"lines": [54, 55, 56, 57], "branches": [[54, 55], [54, 56]]}
# gained: {"lines": [54, 55, 56, 57], "branches": [[54, 55], [54, 56]]}

import pytest
from pymonet.maybe import Maybe

def test_map_with_nothing():
    maybe_nothing = Maybe.nothing()
    result = maybe_nothing.map(lambda x: x * 2)
    assert result.is_nothing

def test_map_with_just():
    maybe_just = Maybe.just(10)
    result = maybe_just.map(lambda x: x * 2)
    assert not result.is_nothing
    assert result.value == 20
