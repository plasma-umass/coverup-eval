# file pypara/dcc.py:522-545
# lines [522, 523, 545]
# branches []

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_act_365_a
from datetime import date

@pytest.fixture
def mock_has_leap_day(mocker):
    mocker.patch('pypara.dcc._has_leap_day', return_value=True)

def test_dcfc_act_365_a_with_leap_day(mock_has_leap_day):
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 29)  # Leap day
    end_date = asof_date
    expected_dcf = Decimal('0.17213114754098')
    dcf = dcfc_act_365_a(start=start_date, asof=asof_date, end=end_date)
    assert round(dcf, 14) == expected_dcf
