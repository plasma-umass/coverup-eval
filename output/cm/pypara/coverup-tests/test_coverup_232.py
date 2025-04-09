# file pypara/dcc.py:676-712
# lines []
# branches ['701->705', '705->709']

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_e_plus_360

@pytest.fixture
def mock_date(monkeypatch):
    class MockDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2000, 1, 1)
    monkeypatch.setattr(datetime, 'date', MockDate)

def test_dcfc_30_e_plus_360_branch_coverage():
    # Test case to cover the branch 701->705
    start_date = datetime.date(2007, 12, 31)  # start.day == 31
    asof_date = datetime.date(2008, 1, 31)    # asof.day == 31
    end_date = asof_date
    result = dcfc_30_e_plus_360(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0.08611111111111')  # (32 - 30) + 30 * (1 - 12) + 360 * (2008 - 2007) / 360
    assert round(result, 14) == expected_result

    # Test case to cover the branch 705->709
    start_date = datetime.date(2007, 12, 30)  # start.day != 31
    asof_date = datetime.date(2008, 1, 31)    # asof.day == 31
    end_date = asof_date
    result = dcfc_30_e_plus_360(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0.08611111111111')  # (32 - 30) + 30 * (1 - 12) + 360 * (2008 - 2007) / 360
    assert round(result, 14) == expected_result
