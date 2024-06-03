# file pypara/dcc.py:467-493
# lines [467, 468, 469, 470, 472, 493]
# branches []

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_360

def test_dcfc_act_360():
    ex1_start, ex1_asof = date(2007, 12, 28), date(2008, 2, 28)
    ex2_start, ex2_asof = date(2007, 12, 28), date(2008, 2, 29)
    ex3_start, ex3_asof = date(2007, 10, 31), date(2008, 11, 30)
    ex4_start, ex4_asof = date(2008, 2, 1), date(2009, 5, 31)

    assert round(dcfc_act_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.17222222222222')
    assert round(dcfc_act_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17500000000000')
    assert round(dcfc_act_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.10000000000000')
    assert round(dcfc_act_360(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.34722222222222')

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mock any global state or dependencies here if necessary
    yield
    # Cleanup code here if necessary
