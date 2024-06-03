# file pypara/dcc.py:496-519
# lines [496, 497, 519]
# branches []

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f

def test_dcfc_act_365_f():
    # Test case 1
    ex1_start, ex1_asof = date(2007, 12, 28), date(2008, 2, 28)
    result = round(dcfc_act_365_f(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)
    assert result == Decimal('0.16986301369863')

    # Test case 2
    ex2_start, ex2_asof = date(2007, 12, 28), date(2008, 2, 29)
    result = round(dcfc_act_365_f(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14)
    assert result == Decimal('0.17260273972603')

    # Test case 3
    ex3_start, ex3_asof = date(2007, 10, 31), date(2008, 11, 30)
    result = round(dcfc_act_365_f(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14)
    assert result == Decimal('1.08493150684932')

    # Test case 4
    ex4_start, ex4_asof = date(2008, 2, 1), date(2009, 5, 31)
    result = round(dcfc_act_365_f(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14)
    assert result == Decimal('1.32876712328767')
