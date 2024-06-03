# file pymonet/semigroups.py:64-81
# lines [64, 65, 69, 71, 72, 74, 81]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class TestOne:
    def test_concat(self):
        class One(Semigroup):
            neutral_element = False

            def __init__(self, value):
                self.value = value

            def __str__(self):
                return 'One[value={}]'.format(self.value)

            def concat(self, semigroup):
                return One(self.value or semigroup.value)

        one_true = One(True)
        one_false = One(False)
        one_none = One(None)

        # Test concatenation with True and False
        result = one_true.concat(one_false)
        assert result.value is True
        assert str(result) == 'One[value=True]'

        # Test concatenation with False and True
        result = one_false.concat(one_true)
        assert result.value is True
        assert str(result) == 'One[value=True]'

        # Test concatenation with False and False
        result = one_false.concat(one_false)
        assert result.value is False
        assert str(result) == 'One[value=False]'

        # Test concatenation with None and False
        result = one_none.concat(one_false)
        assert result.value is False
        assert str(result) == 'One[value=False]'

        # Test concatenation with None and True
        result = one_none.concat(one_true)
        assert result.value is True
        assert str(result) == 'One[value=True]'
