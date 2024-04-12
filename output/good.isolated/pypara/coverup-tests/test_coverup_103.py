# file pypara/monetary.py:491-494
# lines [491, 493, 494]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Currency, Money

# Assuming Currency and Date are defined in the pypara.monetary module
# and have the necessary properties for this test to run.

@pytest.fixture
def mock_currency(mocker):
    # Mocking Currency object with a quantizer for Decimal operations
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.quantizer = Decimal('0.01')  # Example quantizer for currency
    return mock_currency

def test_scalar_subtract(mock_currency):
    # Setup
    qty = Decimal('100.00')
    dov = date.today()
    some_money = SomeMoney(mock_currency, qty, dov)

    # Execute
    result = some_money.scalar_subtract(10)

    # Verify
    assert isinstance(result, Money), "Result should be an instance of Money"
    assert result.ccy == mock_currency, "Currency should match the original"
    assert result.qty == Decimal('90.00').quantize(mock_currency.quantizer), "Quantity should be reduced by 10 and quantized"
    assert result.dov == dov, "Date of value should remain unchanged"

    # Cleanup is not necessary as no external state is modified
