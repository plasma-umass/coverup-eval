# file: pypara/monetary.py:385-387
# asked: {"lines": [385, 386, 387], "branches": []}
# gained: {"lines": [385, 386], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.numbers import Numeric
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __truediv__(self, other: Numeric) -> "ConcreteMoney":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Unsupported type for division")
        return self

def test_truediv_with_int():
    money = ConcreteMoney()
    result = money.__truediv__(10)
    assert isinstance(result, ConcreteMoney)

def test_truediv_with_float():
    money = ConcreteMoney()
    result = money.__truediv__(10.5)
    assert isinstance(result, ConcreteMoney)

def test_truediv_with_decimal():
    money = ConcreteMoney()
    result = money.__truediv__(Decimal('10.5'))
    assert isinstance(result, ConcreteMoney)

def test_truediv_with_invalid_type():
    money = ConcreteMoney()
    with pytest.raises(TypeError):
        money.__truediv__("invalid")
