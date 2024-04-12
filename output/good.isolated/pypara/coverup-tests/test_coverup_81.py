# file pypara/monetary.py:190-197
# lines [190, 191, 197]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal
from numbers import Number

class Numeric(Number):
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        if isinstance(other, Numeric):
            return Numeric(self.value - other.value)
        return NotImplemented

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = Decimal(amount)

    def scalar_subtract(self, other: Numeric) -> "Money":
        if not isinstance(other, Numeric):
            raise TypeError("The 'other' must be an instance of Numeric")
        return ConcreteMoney(self.amount - Decimal(other.value))

@pytest.fixture
def mock_numeric():
    return Numeric(10)

def test_scalar_subtract(mock_numeric):
    money = ConcreteMoney(100)
    result = money.scalar_subtract(mock_numeric)
    assert result.amount == Decimal(90), "The scalar subtraction result should be 90"

def test_scalar_subtract_with_non_numeric():
    money = ConcreteMoney(100)
    with pytest.raises(TypeError):
        money.scalar_subtract(10)  # 10 is not an instance of Numeric

# Clean up is not necessary as no global state is modified in these tests
