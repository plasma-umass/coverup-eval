# file pymonet/semigroups.py:44-61
# lines [44, 45, 49, 51, 52, 54, 61]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class TestAllSemigroup:
    def test_all_concat(self):
        class All(Semigroup):
            neutral_element = True

            def __str__(self) -> str:
                return 'All[value={}]'.format(self.value)

            def concat(self, semigroup: 'All') -> 'All':
                return All(self.value and semigroup.value)

        # Test cases for concat method
        all_true = All(True)
        all_false = All(False)

        result = all_true.concat(all_true)
        assert result.value is True, "Expected True but got {}".format(result.value)

        result = all_true.concat(all_false)
        assert result.value is False, "Expected False but got {}".format(result.value)

        result = all_false.concat(all_true)
        assert result.value is False, "Expected False but got {}".format(result.value)

        result = all_false.concat(all_false)
        assert result.value is False, "Expected False but got {}".format(result.value)

    def test_all_str(self):
        class All(Semigroup):
            neutral_element = True

            def __str__(self) -> str:
                return 'All[value={}]'.format(self.value)

            def concat(self, semigroup: 'All') -> 'All':
                return All(self.value and semigroup.value)

        all_instance = All(True)
        assert str(all_instance) == 'All[value=True]', "Expected 'All[value=True]' but got {}".format(str(all_instance))

        all_instance = All(False)
        assert str(all_instance) == 'All[value=False]', "Expected 'All[value=False]' but got {}".format(str(all_instance))
