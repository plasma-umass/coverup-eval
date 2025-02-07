# file: pymonet/monad_try.py:14-17
# asked: {"lines": [14, 15, 16, 17], "branches": []}
# gained: {"lines": [14, 15, 16, 17], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_eq():
    # Create instances of Try
    try1 = Try(value=10, is_success=True)
    try2 = Try(value=10, is_success=True)
    try3 = Try(value=20, is_success=True)
    try4 = Try(value=10, is_success=False)
    try5 = "Not a Try instance"

    # Test equality
    assert try1 == try2  # Should be True
    assert try1 != try3  # Should be True
    assert try1 != try4  # Should be True
    assert try1 != try5  # Should be True

    # Clean up
    del try1, try2, try3, try4, try5
