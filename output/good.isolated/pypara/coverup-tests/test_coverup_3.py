# file pypara/dcc.py:467-493
# lines [467, 468, 469, 470, 472, 493]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.dcc import dcfc_act_360

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Teardown code if necessary

def test_dcfc_act_360(cleanup):
    start_date = date(2020, 1, 1)
    asof_date = date(2020, 1, 31)
    end_date = date(2020, 1, 31)
    expected_result = Decimal('0.08333333333333')  # (31 - 1) / 360
    result = dcfc_act_360(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == expected_result
