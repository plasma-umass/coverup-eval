# file: pymonet/semigroups.py:84-99
# asked: {"lines": [84, 85, 89, 90, 92, 99], "branches": []}
# gained: {"lines": [84, 85, 89, 90, 92, 99], "branches": []}

import pytest
from pymonet.semigroups import First, Semigroup

def test_first_concat():
    first1 = First(1)
    first2 = First(2)
    result = first1.concat(first2)
    
    assert isinstance(result, First)
    assert result.value == 1

def test_first_str():
    first = First(1)
    assert str(first) == 'Fist[value=1]'
