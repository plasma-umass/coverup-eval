# file: pypara/monetary.py:1390-1391
# asked: {"lines": [1390, 1391], "branches": []}
# gained: {"lines": [1390, 1391], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.commons.zeitgeist import Date

def test_noneprice_with_dov():
    # Create an instance of NonePrice
    none_price = NonePrice()

    # Create a Date instance
    dov = Date.today()

    # Call the with_dov method
    result = none_price.with_dov(dov)

    # Assert that the result is the same instance of NonePrice
    assert result is none_price
