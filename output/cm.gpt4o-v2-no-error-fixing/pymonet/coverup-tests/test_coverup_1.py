# file: pymonet/maybe.py:114-125
# asked: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}
# gained: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_maybe_to_either_with_value():
    maybe = Maybe.just(10)
    either = maybe.to_either()
    assert isinstance(either, Right)
    assert either.value == 10

def test_maybe_to_either_with_nothing():
    maybe = Maybe.nothing()
    either = maybe.to_either()
    assert isinstance(either, Left)
    assert either.value is None
