# file pypara/monetary.py:860-871
# lines [871]
# branches []

import pytest
from pypara.monetary import Price, IncompatibleCurrencyError

class ConcretePrice(Price):
    def subtract(self, other: "Price") -> "Price":
        return super().subtract(other)

def test_price_subtract_not_implemented(mocker):
    price1 = ConcretePrice()
    price2 = ConcretePrice()
    
    with pytest.raises(NotImplementedError):
        price1.subtract(price2)
