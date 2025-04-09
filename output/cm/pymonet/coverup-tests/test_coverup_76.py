# file pymonet/semigroups.py:1-21
# lines [1, 2, 10, 11, 13, 14, 16, 17, 19, 20, 21]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class TestSemigroup:
    def test_semigroup_equality(self):
        # Test the equality method of Semigroup class
        semigroup1 = Semigroup(10)
        semigroup2 = Semigroup(10)
        semigroup3 = Semigroup(20)

        assert semigroup1 == semigroup2, "Semigroup equality failed when values are the same"
        assert not (semigroup1 == semigroup3), "Semigroup equality failed when values are different"

    def test_semigroup_fold(self):
        # Test the fold method of Semigroup class
        semigroup = Semigroup(10)
        result = semigroup.fold(lambda x: x * 2)

        assert result == 20, "Semigroup fold method failed to apply the function correctly"

    def test_semigroup_neutral(self):
        # Test the neutral method of Semigroup class
        # Since the neutral_element is not defined in the Semigroup class,
        # we cannot test the neutral method as it is. We need to create a subclass
        # that defines the neutral_element or skip this test.
        class SemigroupWithNeutral(Semigroup):
            neutral_element = 0

        neutral_semigroup = SemigroupWithNeutral.neutral()

        assert isinstance(neutral_semigroup, Semigroup), "Semigroup neutral method did not return a Semigroup instance"
        assert neutral_semigroup.value == 0, "Semigroup neutral method did not return the neutral element"

# The following code is not part of the test script and should not be included in the response
# if __name__ == "__main__":
#     pytest.main()
