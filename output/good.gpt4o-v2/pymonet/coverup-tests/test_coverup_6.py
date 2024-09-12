# file: pymonet/maybe.py:114-125
# asked: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}
# gained: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_to_either_with_nothing():
    maybe_nothing = Maybe.nothing()
    either_result = maybe_nothing.to_either()
    
    assert isinstance(either_result, Left)
    assert either_result.value is None

def test_to_either_with_just():
    value = 42
    maybe_just = Maybe.just(value)
    either_result = maybe_just.to_either()
    
    assert isinstance(either_result, Right)
    assert either_result.value == value
