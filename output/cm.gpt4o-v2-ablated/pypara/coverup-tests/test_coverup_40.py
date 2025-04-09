# file: pypara/monetary.py:1345-1346
# asked: {"lines": [1345, 1346], "branches": []}
# gained: {"lines": [1345, 1346], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price_positive():
    none_price = NonePrice()
    result = none_price.positive()
    assert result is none_price

# Assuming NonePrice inherits from Price and does not add any additional state,
# there is no need for further cleanup or state management.
