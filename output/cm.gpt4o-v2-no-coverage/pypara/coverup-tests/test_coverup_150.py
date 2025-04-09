# file: pypara/monetary.py:1119-1120
# asked: {"lines": [1119, 1120], "branches": []}
# gained: {"lines": [1119, 1120], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

def test_someprice_as_float():
    mock_ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    mock_qty = Decimal("100.00")
    mock_dov = Date(2023, 1, 1)
    some_price = SomePrice(ccy=mock_ccy, qty=mock_qty, dov=mock_dov)
    
    assert some_price.as_float() == float(mock_qty)
