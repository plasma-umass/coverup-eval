# file: pypara/dcc.py:467-493
# asked: {"lines": [467, 468, 469, 470, 472, 493], "branches": []}
# gained: {"lines": [467, 468, 469, 470, 472, 493], "branches": []}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_act_360
from pypara.commons.zeitgeist import Date

def test_dcfc_act_360():
    ex1_start, ex1_asof = Date(2007, 12, 28), Date(2008, 2, 28)
    ex2_start, ex2_asof = Date(2007, 12, 28), Date(2008, 2, 29)
    ex3_start, ex3_asof = Date(2007, 10, 31), Date(2008, 11, 30)
    ex4_start, ex4_asof = Date(2008, 2, 1), Date(2009, 5, 31)

    assert round(dcfc_act_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.17222222222222')
    assert round(dcfc_act_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17500000000000')
    assert round(dcfc_act_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.10000000000000')
    assert round(dcfc_act_360(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.34722222222222')
