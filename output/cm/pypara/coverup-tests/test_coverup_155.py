# file pypara/monetary.py:545-546
# lines [545, 546]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, 'Test Currency', 2, 'Test Type', Decimal('0.01'), True)

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_with_ccy(cleanup):
    original_ccy = MockCurrency('USD')
    new_ccy = MockCurrency('EUR')
    qty = Decimal('100.00')
    dov = Date(2023, 1, 1)
    money = SomeMoney(original_ccy, qty, dov)

    # Test the with_ccy method
    new_money = money.with_ccy(new_ccy)

    # Assertions to verify postconditions
    assert new_money.ccy == new_ccy
    assert new_money.qty == qty
    assert new_money.dov == dov
