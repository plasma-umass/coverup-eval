# file: pymonet/maybe.py:73-85
# asked: {"lines": [83, 84, 85], "branches": [[83, 84], [83, 85]]}
# gained: {"lines": [83, 84, 85], "branches": [[83, 84], [83, 85]]}

import pytest
from pymonet.maybe import Maybe

def test_ap_with_nothing():
    maybe_nothing = Maybe.nothing()
    applicative = Maybe.just(lambda x: x + 1)
    result = maybe_nothing.ap(applicative)
    assert result.is_nothing

def test_ap_with_just():
    maybe_just = Maybe.just(lambda x: x + 1)
    applicative = Maybe.just(2)
    result = maybe_just.ap(applicative)
    assert result.value == 3

def test_ap_with_nothing_applicative():
    maybe_just = Maybe.just(lambda x: x + 1)
    applicative = Maybe.nothing()
    result = maybe_just.ap(applicative)
    assert result.is_nothing
