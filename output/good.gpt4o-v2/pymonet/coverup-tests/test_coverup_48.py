# file: pymonet/maybe.py:44-58
# asked: {"lines": [44, 54, 55, 56, 57], "branches": [[54, 55], [54, 56]]}
# gained: {"lines": [44, 54, 55, 56, 57], "branches": [[54, 55], [54, 56]]}

import pytest
from pymonet.maybe import Maybe

def test_maybe_map_with_value():
    maybe = Maybe.just(5)
    result = maybe.map(lambda x: x * 2)
    assert hasattr(result, 'value')
    assert result.value == 10
    assert not result.is_nothing

def test_maybe_map_with_nothing():
    maybe = Maybe.nothing()
    result = maybe.map(lambda x: x * 2)
    assert result.is_nothing
    assert not hasattr(result, 'value')
