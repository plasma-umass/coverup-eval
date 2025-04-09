# file: pymonet/maybe.py:24-33
# asked: {"lines": [24, 25, 33], "branches": []}
# gained: {"lines": [24, 25, 33], "branches": []}

import pytest
from pymonet.maybe import Maybe

def test_maybe_just():
    value = 10
    maybe_instance = Maybe.just(value)
    
    assert maybe_instance.is_nothing is False
    assert maybe_instance.value == value
