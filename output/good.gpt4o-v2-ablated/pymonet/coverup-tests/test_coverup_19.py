# file: pymonet/semigroups.py:102-117
# asked: {"lines": [102, 103, 107, 108, 110, 117], "branches": []}
# gained: {"lines": [102, 103, 107, 108, 110, 117], "branches": []}

import pytest
from pymonet.semigroups import Last

def test_last_concat():
    # Create two Last instances
    last1 = Last(1)
    last2 = Last(2)
    
    # Concatenate last1 with last2
    result = last1.concat(last2)
    
    # Assert that the result is a new Last instance with the value of last2
    assert isinstance(result, Last)
    assert result.value == 2

def test_last_str():
    # Create a Last instance
    last = Last(3)
    
    # Assert that the string representation is correct
    assert str(last) == 'Last[value=3]'
