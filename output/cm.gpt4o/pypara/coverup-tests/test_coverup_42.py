# file pypara/dcc.py:676-712
# lines [676, 677, 701, 702, 705, 706, 709, 712]
# branches ['701->702', '701->705', '705->706', '705->709']

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_e_plus_360

def test_dcfc_30_e_plus_360():
    # Test case where start day is 31
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16111111111111')

    # Test case where asof day is 31
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.09166666666667')

    # Test case where both start and asof days are 31
    start = datetime.date(2007, 10, 31)
    asof = datetime.date(2008, 11, 30)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08333333333333')

    # Test case with different dates
    start = datetime.date(2008, 2, 1)
    asof = datetime.date(2009, 5, 31)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.33333333333333')

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
