# file: pymonet/maybe.py:60-71
# asked: {"lines": [60, 69, 70, 71], "branches": [[69, 70], [69, 71]]}
# gained: {"lines": [60, 69, 70, 71], "branches": [[69, 70], [69, 71]]}

import pytest
from pymonet.maybe import Maybe

def test_bind_with_nothing():
    maybe_nothing = Maybe.nothing()
    result = maybe_nothing.bind(lambda x: Maybe.just(x + 1))
    assert result.is_nothing

def test_bind_with_just():
    maybe_just = Maybe.just(5)
    result = maybe_just.bind(lambda x: Maybe.just(x + 1))
    assert not result.is_nothing
    assert result.value == 6
