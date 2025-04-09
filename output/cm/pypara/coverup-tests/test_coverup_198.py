# file pypara/monetary.py:1240-1241
# lines [1240, 1241]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, 'Test Currency', 2, 'ROUND_HALF_UP', True, hashcache=None)

@pytest.fixture
def mock_currency():
    original_currency = MockCurrency('USD')
    new_currency = MockCurrency('EUR')
    return original_currency, new_currency

def test_with_ccy(mock_currency):
    original_ccy, new_ccy = mock_currency
    qty = Decimal('100.00')
    dov = Date(2023, 1, 1)
    price = SomePrice(original_ccy, qty, dov)

    # Call the method that needs coverage
    new_price = price.with_ccy(new_ccy)

    # Assertions to verify postconditions
    assert new_price.ccy == new_ccy
    assert new_price.qty == qty
    assert new_price.dov == dov
