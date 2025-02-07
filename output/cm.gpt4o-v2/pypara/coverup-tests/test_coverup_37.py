# file: pypara/dcc.py:548-571
# asked: {"lines": [548, 549, 571], "branches": []}
# gained: {"lines": [548, 549, 571], "branches": []}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_act_365_l

def test_dcfc_act_365_l():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_act_365_l(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08196721311475')
    assert round(dcfc_act_365_l(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.32876712328767')
