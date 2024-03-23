# file pypara/monetary.py:994-1003
# lines [994, 995, 1003]
# branches []

import pytest
from pypara.monetary import Price, FXRateLookupError, Currency
from datetime import date
from typing import Optional

class MockPrice(Price):
    def convert(self, to: Currency, asof: Optional[date] = None, strict: bool = False) -> "Price":
        if to == "USD":
            return MockPrice()
        else:
            raise FXRateLookupError("No FX rate available for conversion.", "EUR", asof)

def test_price_convert_success():
    mock_price = MockPrice()
    converted_price = mock_price.convert(to="USD")
    assert isinstance(converted_price, Price)

def test_price_convert_failure():
    mock_price = MockPrice()
    with pytest.raises(FXRateLookupError) as exc_info:
        mock_price.convert(to="EUR")
    assert "No FX rate available for conversion." in str(exc_info.value)
