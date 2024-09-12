# file: f002/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f002 import truncate_number

def test_truncate_number():
    # Test with a positive float
    assert truncate_number(123.456) == pytest.approx(0.456, rel=1e-9)
    
    # Test with a negative float
    assert truncate_number(-123.456) == pytest.approx(0.544, rel=1e-9)
    
    # Test with an integer
    assert truncate_number(123) == pytest.approx(0.0, rel=1e-9)
    
    # Test with zero
    assert truncate_number(0) == pytest.approx(0.0, rel=1e-9)
