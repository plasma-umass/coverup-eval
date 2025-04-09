# file: pypara/monetary.py:313-320
# asked: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}
# gained: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, NoMoney, SomeMoney
from typing import Optional
from unittest.mock import patch

@pytest.fixture
def mock_currency():
    class MockCurrency:
        def quantize(self, qty):
            return qty
    return MockCurrency()

def test_money_of_with_none_values():
    assert Money.of(None, Decimal('10.00'), Date.today()) == NoMoney
    assert Money.of('USD', None, Date.today()) == NoMoney
    assert Money.of('USD', Decimal('10.00'), None) == NoMoney

def test_money_of_with_valid_values(mock_currency):
    ccy = mock_currency
    qty = Decimal('10.00')
    dov = Date.today()
    result = Money.of(ccy, qty, dov)
    assert isinstance(result, SomeMoney)
    assert result.ccy == ccy
    assert result.qty == qty
    assert result.dov == dov
