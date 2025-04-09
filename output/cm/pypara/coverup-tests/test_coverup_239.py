# file pypara/dcc.py:638-673
# lines []
# branches ['662->666', '666->670']

import pytest
import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_e_360

@pytest.fixture
def mock_date(monkeypatch):
    class MockDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2000, 1, 1)
    monkeypatch.setattr(datetime, 'date', MockDate)

def test_dcfc_30_e_360_branch_coverage(mock_date):
    # Test the branch where start.day == 31
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 1, 30)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.08333333333333')
    assert round(result, 14) == expected

    # Test the branch where asof.day == 31
    start = datetime.date(2007, 12, 30)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.08333333333333')
    assert round(result, 14) == expected
