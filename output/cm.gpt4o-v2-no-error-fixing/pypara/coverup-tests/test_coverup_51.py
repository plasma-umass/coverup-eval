# file: pypara/monetary.py:665-666
# asked: {"lines": [665, 666], "branches": []}
# gained: {"lines": [665, 666], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

def test_none_money_multiply():
    none_money = NoneMoney()
    result = none_money.multiply(10)
    assert result is none_money
