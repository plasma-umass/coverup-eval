# file pypara/monetary.py:662-663
# lines [662, 663]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_scalar_subtract():
    none_money = NoneMoney()
    result = none_money.scalar_subtract(10)
    assert result is none_money, "The result should be the same NoneMoney instance"
