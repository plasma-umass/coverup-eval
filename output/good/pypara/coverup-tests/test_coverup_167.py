# file pypara/monetary.py:1243-1244
# lines [1243, 1244]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_with_qty(cleanup, mocker):
    # Mocking Currency and Date to avoid dependencies
    mock_currency = mocker.MagicMock(spec=Currency)
    mock_date = mocker.MagicMock(spec=Date)

    # Create an instance of SomePrice
    original_price = SomePrice(mock_currency, Decimal('100.00'), mock_date)

    # Change the quantity using with_qty
    new_qty = Decimal('200.00')
    new_price = original_price.with_qty(new_qty)

    # Assertions to check if the new_price has the updated quantity
    assert new_price.qty == new_qty
    assert new_price.ccy == original_price.ccy
    assert new_price.dov == original_price.dov

    # Cleanup is handled by the fixture
