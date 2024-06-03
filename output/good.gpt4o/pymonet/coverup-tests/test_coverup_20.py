# file pymonet/semigroups.py:140-157
# lines [140, 141, 145, 147, 148, 150, 157]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class Max(Semigroup):
    """
    Max is a Monoid that will combine 2 numbers, resulting in the largest of the two.
    """
    
    neutral_element = -float("inf")
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:  # pragma: no cover
        return 'Max[value={}]'.format(self.value)
    
    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Max[B]
        :returns: new Max with largest value
        :rtype: Max[A | B]
        """
        return Max(self.value if self.value > semigroup.value else semigroup.value)

def test_max_concat():
    max1 = Max(10)
    max2 = Max(20)
    result = max1.concat(max2)
    assert result.value == 20

def test_max_str():
    max_instance = Max(15)
    assert str(max_instance) == 'Max[value=15]'
