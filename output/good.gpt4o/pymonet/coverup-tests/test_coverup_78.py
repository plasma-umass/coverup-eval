# file pymonet/utils.py:37-46
# lines [37, 46]
# branches []

import pytest
from pymonet.utils import increase

def test_increase():
    # Test with a positive integer
    assert increase(1) == 2
    
    # Test with zero
    assert increase(0) == 1
    
    # Test with a negative integer
    assert increase(-1) == 0
    
    # Test with a large integer
    assert increase(1000000) == 1000001
