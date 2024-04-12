# file pypara/monetary.py:1129-1131
# lines [1129, 1130, 1131]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice

# Mocking the Currency class for the purpose of the test
class MockCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

@pytest.fixture
def cleanup():
    # Setup if needed
    yield
    # Cleanup code if needed

def test_someprice_negative(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('100.00')
    dov = date.today()
    price = SomePrice(currency, quantity, dov)

    negative_price = price.negative()

    assert negative_price.ccy == currency
    assert negative_price.qty == -quantity
    assert negative_price.dov == dov
