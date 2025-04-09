# file: pypara/monetary.py:692-693
# asked: {"lines": [692, 693], "branches": []}
# gained: {"lines": [692, 693], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.commons.zeitgeist import Date

def test_none_money_with_dov():
    none_money = NoneMoney()
    dov = Date(2023, 1, 1)
    result = none_money.with_dov(dov)
    assert result is none_money
