# file: pymonet/either.py:106-111
# asked: {"lines": [106, 111], "branches": []}
# gained: {"lines": [106, 111], "branches": []}

import pytest
from pymonet.either import Left, Either

def test_left_ap():
    # Create an instance of Left
    left_instance = Left("error")

    # Apply the ap method
    result = left_instance.ap(None)

    # Assert that the result is still a Left instance with the same value
    assert isinstance(result, Left)
    assert result.value == "error"
