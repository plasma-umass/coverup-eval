# file pymonet/semigroups.py:84-99
# lines [84, 85, 89, 90, 92, 99]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class First(Semigroup):
    """
    First is a Monoid that will always return the first value when 2 First instances are combined.
    """
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:  # pragma: no cover
        return 'First[value={}]'.format(self.value)
    
    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: First[B]
        :returns: new First with first value
        :rtype: First[A]
        """
        return First(self.value)

def test_first_concat():
    first1 = First(10)
    first2 = First(20)
    
    result = first1.concat(first2)
    
    assert isinstance(result, First)
    assert result.value == 10

def test_first_str():
    first = First(10)
    assert str(first) == 'First[value=10]'
