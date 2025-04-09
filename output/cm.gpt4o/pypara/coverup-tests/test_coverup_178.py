# file pypara/monetary.py:994-1003
# lines [1003]
# branches []

from typing import Optional
import pytest
from pypara.monetary import Price, Currency, Date, FXRateLookupError

def test_price_convert_not_implemented():
    class TestPrice(Price):
        def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Price":
            super().convert(to, asof, strict)

    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.convert(Currency('USD', 'US Dollar', 2, 'standard', None, None))

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
