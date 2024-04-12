# file pymonet/monad_try.py:10-12
# lines [10, 11, 12]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_init():
    # Test the successful creation of a Try instance with is_success=True
    try_success = Try(value="Success", is_success=True)
    assert try_success.value == "Success"
    assert try_success.is_success is True

    # Test the creation of a Try instance with is_success=False
    try_failure = Try(value="Failure", is_success=False)
    assert try_failure.value == "Failure"
    assert try_failure.is_success is False

    # Clean up is not necessary as no external resources or state changes are involved
