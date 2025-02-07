# file: pypara/dcc.py:496-519
# asked: {"lines": [496, 497, 519], "branches": []}
# gained: {"lines": [496, 497, 519], "branches": []}

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f
from pypara.commons.zeitgeist import Date

def test_dcfc_act_365_f():
    ex1_start, ex1_asof = Date(2007, 12, 28), Date(2008, 2, 28)
    ex2_start, ex2_asof = Date(2007, 12, 28), Date(2008, 2, 29)
    ex3_start, ex3_asof = Date(2007, 10, 31), Date(2008, 11, 30)
    ex4_start, ex4_asof = Date(2008, 2, 1), Date(2009, 5, 31)

    assert round(dcfc_act_365_f(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')
    assert round(dcfc_act_365_f(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17260273972603')
    assert round(dcfc_act_365_f(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08493150684932')
    assert round(dcfc_act_365_f(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.32876712328767')
