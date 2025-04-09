# file pypara/monetary.py:1122-1123
# lines [1123]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

@pytest.fixture
def cleanup():
    # Setup code if needed
    yield
    # Cleanup code if needed

def test_some_price_as_integer(mocker, cleanup):
    # Mocking Currency and Date as they are not the focus of this test
    mock_currency = mocker.MagicMock(spec=Currency)
    mock_date = mocker.MagicMock(spec=Date)
    
    # Create an instance of SomePrice with a Decimal quantity
    price = SomePrice(ccy=mock_currency, qty=Decimal('123.45'), dov=mock_date)
    
    # Call the as_integer method which should execute line 1123
    result = price.as_integer()
    
    # Assert that the result is an integer and equals the integer part of the Decimal quantity
    assert isinstance(result, int)
    assert result == 123  # Assuming that the as_integer method should truncate the decimal part
