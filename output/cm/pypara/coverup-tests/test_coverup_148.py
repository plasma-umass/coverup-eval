# file pypara/monetary.py:430-431
# lines [430, 431]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, 'Test Currency', 2, 'currency', None, True)

@pytest.fixture
def cleanup():
    # Setup if needed
    yield
    # Cleanup code if needed

def test_as_integer(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('123.45')
    date_of_value = Date(2023, 4, 1)
    some_money = SomeMoney(ccy=currency, qty=quantity, dov=date_of_value)
    
    result = some_money.as_integer()
    
    assert result == 123, "The integer part of the quantity should be returned"
