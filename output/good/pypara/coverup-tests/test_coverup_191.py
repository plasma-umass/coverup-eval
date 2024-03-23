# file pypara/monetary.py:1393-1394
# lines [1393, 1394]
# branches []

import pytest
from pypara.monetary import NonePrice, Currency, Price

@pytest.fixture
def mock_currency(mocker):
    return mocker.create_autospec(Currency)

def test_none_price_convert(mock_currency):
    none_price = NonePrice()
    
    # Test convert method on NonePrice
    result = none_price.convert(mock_currency)
    
    # Assert that the result of convert is the same NonePrice instance
    assert result is none_price

    # Clean up is not necessary as we are using mock objects and not modifying any global state
