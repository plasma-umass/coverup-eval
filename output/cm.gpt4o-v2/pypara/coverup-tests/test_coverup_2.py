# file: pypara/dcc.py:399-440
# asked: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}
# gained: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_act_act
from pypara.commons.zeitgeist import Date

def test_dcfc_act_act():
    ex1_start, ex1_asof = Date(2007, 12, 28), Date(2008, 2, 28)
    ex2_start, ex2_asof = Date(2007, 12, 28), Date(2008, 2, 29)
    ex3_start, ex3_asof = Date(2007, 10, 31), Date(2008, 11, 30)
    ex4_start, ex4_asof = Date(2008, 2, 1), Date(2009, 5, 31)

    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17216108990194')
    assert round(dcfc_act_act(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08243131970956')
    assert round(dcfc_act_act(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.32625945055768')
