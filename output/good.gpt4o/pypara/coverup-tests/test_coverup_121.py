# file pypara/monetary.py:1393-1394
# lines [1393, 1394]
# branches []

import pytest
from pypara.monetary import NonePrice, Currency, Date

def test_none_price_convert():
    # Arrange
    none_price = NonePrice()
    to_currency = Currency("USD", "United States Dollar", 2, "standard", None, None)
    asof_date = Date(2023, 10, 1)
    
    # Act
    result = none_price.convert(to=to_currency, asof=asof_date, strict=True)
    
    # Assert
    assert result is none_price

    # Clean up
    del none_price
    del to_currency
    del asof_date
    del result
