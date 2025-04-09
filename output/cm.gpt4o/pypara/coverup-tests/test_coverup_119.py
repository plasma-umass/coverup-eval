# file pypara/monetary.py:1384-1385
# lines [1384, 1385]
# branches []

import pytest
from pypara.monetary import Price, Currency, NonePrice

def test_noneprice_with_ccy():
    # Arrange
    none_price = NonePrice()
    mock_currency = Currency("USD", "United States Dollar", 2, "fiat", None, None)

    # Act
    result = none_price.with_ccy(mock_currency)

    # Assert
    assert result is none_price
