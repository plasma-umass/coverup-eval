# file pymonet/semigroups.py:1-21
# lines [1, 2, 10, 11, 13, 14, 16, 17, 19, 20, 21]
# branches []

import pytest
from pymonet.semigroups import Semigroup

class TestSemigroup:
    
    def test_semigroup_equality(self):
        sg1 = Semigroup(5)
        sg2 = Semigroup(5)
        sg3 = Semigroup(10)
        
        assert sg1 == sg2
        assert sg1 != sg3

    def test_semigroup_fold(self):
        sg = Semigroup(5)
        result = sg.fold(lambda x: x * 2)
        
        assert result == 10

    def test_semigroup_neutral(self, mocker):
        class TestSemigroup(Semigroup):
            neutral_element = 0
        
        mocker.patch.object(TestSemigroup, 'neutral_element', 0)
        neutral_sg = TestSemigroup.neutral()
        
        assert neutral_sg.value == 0
        assert isinstance(neutral_sg, TestSemigroup)
