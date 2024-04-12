# file pypara/monetary.py:980-985
# lines [980, 981, 985]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import Price

class ConcretePrice(Price):
    def with_qty(self, qty: Decimal) -> "Price":
        return ConcretePrice()

def test_price_with_qty(mocker):
    mocker.patch.object(ConcretePrice, 'with_qty', return_value=ConcretePrice())
    price_instance = ConcretePrice()
    result = price_instance.with_qty(Decimal('2'))
    assert isinstance(result, Price)
    ConcretePrice.with_qty.assert_called_once_with(Decimal('2'))
