# file pymonet/semigroups.py:160-177
# lines [160, 161, 165, 167, 168, 170, 177]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class Min(Semigroup):
    """
    Min is a Monoid that will combines 2 numbers, resulting in the smallest of the two.
    """
    
    neutral_element = float("inf")
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:  # pragma: no cover
        return 'Min[value={}]'.format(self.value)
    
    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Min[B]
        :returns: new Min with smallest value
        :rtype: Min[A | B]
        """
        return Min(self.value if self.value <= semigroup.value else semigroup.value)

def test_min_concat():
    min1 = Min(10)
    min2 = Min(20)
    result = min1.concat(min2)
    assert result.value == 10

    min3 = Min(5)
    result = min1.concat(min3)
    assert result.value == 5

def test_min_str():
    min1 = Min(10)
    assert str(min1) == 'Min[value=10]'
