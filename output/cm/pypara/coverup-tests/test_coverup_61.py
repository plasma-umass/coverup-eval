# file pypara/monetary.py:389-391
# lines [389, 390, 391]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal
from typing import Union

Numeric = Union[int, float, Decimal]

class ConcreteMoney(Money):
    def __init__(self, amount: Numeric):
        self.amount = amount

    def __floordiv__(self, other: Numeric) -> "ConcreteMoney":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Operand must be a numeric type")
        return ConcreteMoney(self.amount // other)

@pytest.fixture
def mock_money():
    return ConcreteMoney(100)

def test_money_floordiv(mock_money):
    result = mock_money // 5
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 20

    with pytest.raises(TypeError):
        mock_money // "invalid"

    # Clean up if necessary (not needed in this case as no external resources are used)
