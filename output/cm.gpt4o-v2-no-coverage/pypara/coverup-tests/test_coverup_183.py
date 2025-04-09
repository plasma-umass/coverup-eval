# file: pypara/monetary.py:427-428
# asked: {"lines": [428], "branches": []}
# gained: {"lines": [428], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency
from pypara.monetary import SomeMoney

class MockCurrency(Currency):
    @classmethod
    def of(cls, code, name, decimals, ctype):
        return super().__new__(cls, code, name, decimals, ctype, Decimal('1.' + '0' * decimals), hash((code, name, decimals, ctype)))

@pytest.fixture
def some_money():
    ccy = MockCurrency.of("USD", "US Dollar", 2, "MONEY")
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    return SomeMoney(ccy, qty, dov)

def test_as_float(some_money):
    result = some_money.as_float()
    assert result == 100.00
