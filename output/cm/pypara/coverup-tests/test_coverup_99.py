# file pypara/monetary.py:217-225
# lines [217, 218, 225]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal, InvalidOperation

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = Decimal(amount)

    def floor_divide(self, other):
        if other == 0:
            return ConcreteMoney('NaN')  # Undefined money object
        try:
            return ConcreteMoney(self.amount // Decimal(other))
        except InvalidOperation:
            raise TypeError("Invalid type for floor division")

def test_floor_divide():
    money = ConcreteMoney(100)
    result = money.floor_divide(3)
    assert result.amount == Decimal(33)  # 100 // 3 == 33

    result = money.floor_divide(0)
    assert result.amount.is_nan()  # Division by zero yields undefined money object

    with pytest.raises(TypeError):
        money.floor_divide('invalid')  # Should raise TypeError due to invalid type
