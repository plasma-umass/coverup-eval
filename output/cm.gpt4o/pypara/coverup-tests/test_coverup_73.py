# file pypara/monetary.py:641-642
# lines [641, 642]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def as_integer(self) -> int:
        raise TypeError("Undefined monetary values do not have quantity information.")

def test_none_money_as_integer():
    none_money = NoneMoney()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_money.as_integer()
