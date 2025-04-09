# file: pymonet/either.py:189-198
# asked: {"lines": [189, 196, 198], "branches": []}
# gained: {"lines": [189, 196, 198], "branches": []}

import pytest
from pymonet.either import Right
from pymonet.maybe import Maybe

def test_right_to_maybe():
    # Create a Right instance with a value
    right_instance = Right(42)
    
    # Convert Right to Maybe
    maybe_instance = right_instance.to_maybe()
    
    # Assert that the Maybe instance is not nothing and has the correct value
    assert not maybe_instance.is_nothing
    assert maybe_instance.value == 42
