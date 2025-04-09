# file pymonet/semigroups.py:102-117
# lines [102, 103, 107, 108, 110, 117]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class Last(Semigroup):
    """
    Last is a Monoid that will always return the lastest, value when 2 Last instances are combined.
    """

    def __str__(self) -> str:  # pragma: no cover
        return 'Last[value={}]'.format(self.value)

    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Last[B]
        :returns: new Last with last value
        :rtype: Last[A]
        """
        return Last(semigroup.value)

def test_last_concat():
    last1 = Last(1)
    last2 = Last(2)
    result = last1.concat(last2)
    assert isinstance(result, Last)
    assert result.value == 2

def test_last_str():
    last = Last(3)
    assert str(last) == 'Last[value=3]'
