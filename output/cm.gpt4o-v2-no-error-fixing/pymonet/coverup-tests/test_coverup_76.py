# file: pymonet/maybe.py:24-33
# asked: {"lines": [24, 25, 33], "branches": []}
# gained: {"lines": [24, 25, 33], "branches": []}

import pytest
from pymonet.maybe import Maybe

def test_maybe_just():
    # Test that Maybe.just creates a Maybe instance with the correct value and is_nothing set to False
    value = 42
    maybe_instance = Maybe.just(value)
    
    assert isinstance(maybe_instance, Maybe)
    assert maybe_instance.value == value
    assert not maybe_instance.is_nothing
