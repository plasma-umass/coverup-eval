# file pypara/monetary.py:555-582
# lines [569]
# branches ['566->569']

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Currency, FXRateService, ProgrammingError

def test_some_money_convert_raises_attribute_error(mocker):
    # Mock the FXRateService.default to be not None but without a query method
    mock_fx_service = mocker.Mock()
    del mock_fx_service.query
    FXRateService.default = mock_fx_service

    # Create a Currency instance with all required arguments
    ccy = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    to = Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty, dov)

    # Ensure that the AttributeError is raised
    with pytest.raises(AttributeError):
        some_money.convert(to)

    # Clean up by resetting FXRateService.default
    FXRateService.default = None
