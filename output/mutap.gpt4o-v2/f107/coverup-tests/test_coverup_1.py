# file: f107/__init__.py:1-14
# asked: {"lines": [1, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [1, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest
from f107 import even_odd_palindrome

def test_even_odd_palindrome():
    # Test with n = 10
    result = even_odd_palindrome(10)
    assert result == (4, 5), f"Expected (4, 5) but got {result}"

    # Test with n = 1
    result = even_odd_palindrome(1)
    assert result == (0, 1), f"Expected (0, 1) but got {result}"

    # Test with n = 0
    result = even_odd_palindrome(0)
    assert result == (0, 0), f"Expected (0, 0) but got {result}"

    # Test with n = 11
    result = even_odd_palindrome(11)
    assert result == (4, 6), f"Expected (4, 6) but got {result}"

    # Test with n = 20
    result = even_odd_palindrome(20)
    assert result == (4, 6), f"Expected (4, 6) but got {result}"
