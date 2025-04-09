# file: pypara/monetary.py:644-645
# asked: {"lines": [644, 645], "branches": []}
# gained: {"lines": [644, 645], "branches": []}

import pytest
from pypara.monetary import NoneMoney

def test_none_money_round():
    none_money = NoneMoney()
    result = none_money.round()
    assert result is none_money

    result_with_digits = none_money.round(2)
    assert result_with_digits is none_money
