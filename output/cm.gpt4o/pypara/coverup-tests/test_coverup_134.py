# file pypara/monetary.py:168-175
# lines [175]
# branches []

import pytest
from pypara.monetary import Money

def test_scalar_add_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.scalar_add(10)
