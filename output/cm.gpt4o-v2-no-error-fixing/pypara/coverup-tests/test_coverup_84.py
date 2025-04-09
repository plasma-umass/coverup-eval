# file: pypara/monetary.py:190-197
# asked: {"lines": [197], "branches": []}
# gained: {"lines": [197], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

def test_money_scalar_subtract_not_implemented():
    class TestMoney(Money):
        def scalar_subtract(self, other: Numeric) -> "Money":
            return super().scalar_subtract(other)
    
    test_money = TestMoney()
    with pytest.raises(NotImplementedError):
        test_money.scalar_subtract(10)
