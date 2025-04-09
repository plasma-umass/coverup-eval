# file: pymonet/maybe.py:60-71
# asked: {"lines": [69, 70, 71], "branches": [[69, 70], [69, 71]]}
# gained: {"lines": [69, 70, 71], "branches": [[69, 70], [69, 71]]}

import pytest
from pymonet.maybe import Maybe

class MockMaybe(Maybe):
    def __init__(self, value=None, is_nothing=False):
        self._value = value
        self._is_nothing = is_nothing

    @property
    def is_nothing(self):
        return self._is_nothing

    @property
    def value(self):
        return self._value

def test_maybe_bind_nothing():
    maybe_instance = MockMaybe(is_nothing=True)
    result = maybe_instance.bind(lambda x: Maybe.just(x + 1))
    assert result.is_nothing

def test_maybe_bind_just():
    maybe_instance = MockMaybe(value=5, is_nothing=False)
    result = maybe_instance.bind(lambda x: Maybe.just(x + 1))
    assert not result.is_nothing
    assert result.value == 6
