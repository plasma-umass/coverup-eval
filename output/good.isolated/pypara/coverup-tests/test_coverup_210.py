# file pypara/monetary.py:322-328
# lines [328]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    @property
    def price(self):
        return super().price

def test_money_price_not_implemented():
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        _ = money.price
