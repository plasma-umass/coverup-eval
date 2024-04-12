# file pypara/monetary.py:644-645
# lines [644, 645]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_round():
    none_money = NoneMoney()
    rounded_none_money = none_money.round(2)
    assert isinstance(rounded_none_money, Money), "The rounded value should still be a Money instance"
    assert rounded_none_money is none_money, "The rounded NoneMoney should return itself"
