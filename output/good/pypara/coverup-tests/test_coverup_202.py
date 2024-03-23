# file pypara/monetary.py:177-188
# lines [188]
# branches []

import pytest
from pypara.monetary import Money, IncompatibleCurrencyError

class ConcreteMoney(Money):
    def subtract(self, other: "Money") -> "Money":
        return super().subtract(other)

def test_subtract_not_implemented(mocker):
    concrete_money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        concrete_money.subtract(concrete_money)
