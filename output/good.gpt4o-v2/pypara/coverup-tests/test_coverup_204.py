# file: pypara/dcc.py:220-237
# asked: {"lines": [225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}
# gained: {"lines": [225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}

import pytest
from decimal import Decimal
from pypara.dcc import DCC
from pypara.commons.zeitgeist import Date
from pypara.commons.numbers import ZERO
from pypara.currencies import Currency, CurrencyType

class MockDCC(DCC):
    def calculate_fraction_method(self, start, asof, end, freq):
        return Decimal('0.5')

@pytest.fixture
def mock_dcc():
    usd_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return MockDCC(
        name="MockDCC",
        altnames=set(),
        currencies=set([usd_currency]),
        calculate_fraction_method=None
    )

def test_calculate_daily_fraction_before_start(mock_dcc):
    start = Date(2023, 1, 1)
    asof = Date(2022, 12, 31)
    end = Date(2023, 12, 31)
    result = mock_dcc.calculate_daily_fraction(start, asof, end)
    assert result == Decimal('0.5')

def test_calculate_daily_fraction_after_start(mock_dcc):
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 12, 31)
    result = mock_dcc.calculate_daily_fraction(start, asof, end)
    assert result == Decimal('0.0')
