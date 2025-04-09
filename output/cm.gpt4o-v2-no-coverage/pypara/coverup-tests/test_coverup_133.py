# file: pypara/monetary.py:1339-1340
# asked: {"lines": [1339, 1340], "branches": []}
# gained: {"lines": [1339, 1340], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_round():
    price = NonePrice()
    result = price.round(2)
    assert result is price
