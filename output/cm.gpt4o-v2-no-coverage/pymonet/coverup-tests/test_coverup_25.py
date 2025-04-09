# file: pymonet/maybe.py:87-99
# asked: {"lines": [87, 97, 98, 99], "branches": [[97, 98], [97, 99]]}
# gained: {"lines": [87, 97, 98, 99], "branches": [[97, 98], [97, 99]]}

import pytest
from pymonet.maybe import Maybe

def test_filter_with_value_passing_filter():
    maybe = Maybe.just(10)
    result = maybe.filter(lambda x: x > 5)
    assert result == maybe

def test_filter_with_value_failing_filter():
    maybe = Maybe.just(10)
    result = maybe.filter(lambda x: x < 5)
    assert result == Maybe.nothing()

def test_filter_on_nothing():
    maybe = Maybe.nothing()
    result = maybe.filter(lambda x: x > 5)
    assert result == maybe
