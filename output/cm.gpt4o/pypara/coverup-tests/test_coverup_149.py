# file pypara/dcc.py:86-146
# lines [143]
# branches ['142->143']

import datetime
import pytest
from decimal import Decimal
from pypara.dcc import _last_payment_date

def test_last_payment_date_edge_case():
    # Test case to cover the line 143
    start_date = datetime.date(1, 1, 1)
    asof_date = datetime.date(1, 1, 1)
    frequency = 1
    eom = -1  # This will trigger the condition where eom < 1

    result = _last_payment_date(start_date, asof_date, frequency, eom)
    
    # Assert that the function returns the start date as expected
    assert result == start_date

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup code: nothing to setup in this case
    yield
    # Teardown code: nothing to teardown in this case
