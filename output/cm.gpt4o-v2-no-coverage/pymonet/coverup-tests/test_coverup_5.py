# file: pymonet/maybe.py:114-125
# asked: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}
# gained: {"lines": [114, 121, 123, 124, 125], "branches": [[123, 124], [123, 125]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_to_either_with_value():
    maybe = Maybe(10, False)
    result = maybe.to_either()
    assert isinstance(result, Right)
    assert result.value == 10

def test_to_either_with_nothing():
    maybe = Maybe(None, True)
    result = maybe.to_either()
    assert isinstance(result, Left)
    assert result.value is None
