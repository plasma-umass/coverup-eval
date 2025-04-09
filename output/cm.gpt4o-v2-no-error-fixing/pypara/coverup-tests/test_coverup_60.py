# file: pypara/monetary.py:692-693
# asked: {"lines": [692, 693], "branches": []}
# gained: {"lines": [692, 693], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.commons.zeitgeist import Date

def test_none_money_with_dov():
    # Create an instance of NoneMoney
    none_money = NoneMoney()

    # Create a Date instance
    dov = Date.today()

    # Call the with_dov method
    result = none_money.with_dov(dov)

    # Assert that the result is the same instance of NoneMoney
    assert result is none_money
