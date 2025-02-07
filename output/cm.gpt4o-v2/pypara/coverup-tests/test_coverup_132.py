# file: pypara/monetary.py:668-669
# asked: {"lines": [668, 669], "branches": []}
# gained: {"lines": [668, 669], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

def test_none_money_divide():
    none_money = NoneMoney()
    result = none_money.divide(Decimal('1.0'))
    assert result is none_money
