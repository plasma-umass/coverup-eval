# file pypara/monetary.py:217-225
# lines [225]
# branches []

import pytest
from pypara.monetary import Money

def test_money_floor_divide_not_implemented():
    class TestMoney(Money):
        def floor_divide(self, other):
            super().floor_divide(other)
    
    test_money = TestMoney()
    with pytest.raises(NotImplementedError):
        test_money.floor_divide(10)
