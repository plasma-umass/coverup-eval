# file: pypara/monetary.py:1381-1382
# asked: {"lines": [1381, 1382], "branches": []}
# gained: {"lines": [1381, 1382], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, undefined):
        self.undefined = undefined

@pytest.fixture
def mock_price_true():
    return MockPrice(True)

@pytest.fixture
def mock_price_false():
    return MockPrice(False)

def test_none_price_gte_true(mock_price_true):
    none_price = NonePrice()
    assert none_price.gte(mock_price_true) == True

def test_none_price_gte_false(mock_price_false):
    none_price = NonePrice()
    assert none_price.gte(mock_price_false) == False
