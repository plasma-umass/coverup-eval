# file: pypara/monetary.py:1372-1373
# asked: {"lines": [1372, 1373], "branches": []}
# gained: {"lines": [1372, 1373], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, defined):
        self.defined = defined

@pytest.fixture
def mock_price_true():
    return MockPrice(defined=True)

@pytest.fixture
def mock_price_false():
    return MockPrice(defined=False)

def test_none_price_lt_with_defined_true(mock_price_true):
    none_price = NonePrice()
    assert none_price.lt(mock_price_true) == True

def test_none_price_lt_with_defined_false(mock_price_false):
    none_price = NonePrice()
    assert none_price.lt(mock_price_false) == False
