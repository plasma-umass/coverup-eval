# file: pypara/monetary.py:662-663
# asked: {"lines": [662, 663], "branches": []}
# gained: {"lines": [662, 663], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

def test_none_money_scalar_subtract():
    none_money = NoneMoney()
    result = none_money.scalar_subtract(10)
    assert result is none_money
