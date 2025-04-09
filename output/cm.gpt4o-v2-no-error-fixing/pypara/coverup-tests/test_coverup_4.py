# file: pypara/dcc.py:220-237
# asked: {"lines": [220, 225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}
# gained: {"lines": [220, 225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}

import pytest
from decimal import Decimal
from pypara.commons.numbers import ZERO
from pypara.commons.zeitgeist import Date
from pypara.dcc import DCC

class MockDCC(DCC):
    def calculate_fraction_method(self, start, asof, end, freq):
        return Decimal('0.5')

@pytest.fixture
def mock_dcc():
    return MockDCC(name="MockDCC", altnames=set(), currencies=set(), calculate_fraction_method=MockDCC.calculate_fraction_method)

def test_calculate_daily_fraction_before_start(mock_dcc):
    start = Date(2023, 1, 10)
    asof = Date(2023, 1, 9)
    end = Date(2023, 12, 31)
    result = mock_dcc.calculate_daily_fraction(start, asof, end)
    assert result == Decimal('0.5') - ZERO

def test_calculate_daily_fraction_after_start(mock_dcc):
    start = Date(2023, 1, 10)
    asof = Date(2023, 1, 11)
    end = Date(2023, 12, 31)
    result = mock_dcc.calculate_daily_fraction(start, asof, end)
    assert result == Decimal('0.5') - Decimal('0.5')
