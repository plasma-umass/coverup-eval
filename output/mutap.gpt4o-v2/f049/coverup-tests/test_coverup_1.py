# file: f049/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest
from f049 import modp

def test_modp():
    assert modp(0, 5) == 1  # Test with n=0, should return 1
    assert modp(1, 5) == 2  # Test with n=1, p=5, should return 2
    assert modp(2, 5) == 4  # Test with n=2, p=5, should return 4
    assert modp(3, 5) == 3  # Test with n=3, p=5, should return 3
    assert modp(4, 5) == 1  # Test with n=4, p=5, should return 1

    # Test with larger values
    assert modp(10, 7) == 2  # Test with n=10, p=7, should return 2
    assert modp(20, 11) == 1  # Test with n=20, p=11, should return 1
