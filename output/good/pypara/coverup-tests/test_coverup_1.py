# file pypara/dcc.py:757-805
# lines [757, 758, 781, 782, 785, 787, 790, 791, 794, 795, 798, 799, 802, 805]
# branches ['785->787', '785->794', '790->791', '790->794', '794->795', '794->798', '798->799', '798->802']

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_30_360_us
from datetime import date

@pytest.fixture
def mock_is_last_day_of_month(mocker):
    mocker.patch('pypara.dcc._is_last_day_of_month', return_value=True)

def test_dcfc_30_360_us_last_day_of_month(mock_is_last_day_of_month):
    start = date(2007, 12, 31)
    asof = date(2008, 1, 31)
    end = asof
    result = dcfc_30_360_us(start=start, asof=asof, end=end)
    expected = Decimal('1') / Decimal('12')  # 30/360
    assert result == expected
