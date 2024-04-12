# file pypara/monetary.py:1081-1083
# lines [1081, 1082, 1083]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal
from typing import Union

Numeric = Union[int, Decimal]

class ConcretePrice(Price):
    def __init__(self, amount: Numeric):
        self.amount = amount

    def __floordiv__(self, other: Numeric) -> "ConcretePrice":
        return ConcretePrice(self.amount // other)

@pytest.fixture
def mock_price(mocker):
    return mocker.MagicMock(spec=ConcretePrice)

def test_price_floordiv(mock_price):
    # Given a concrete price with a specific amount
    price = ConcretePrice(Decimal('100.00'))
    divisor = Decimal('3')

    # When we use the floor division operator
    result = price // divisor

    # Then we expect the result to be a ConcretePrice instance with the correct amount
    assert isinstance(result, ConcretePrice)
    assert result.amount == Decimal('33')

    # Cleanup is not necessary as we are not modifying any global state
