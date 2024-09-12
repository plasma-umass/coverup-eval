# file: pypara/dcc.py:574-597
# asked: {"lines": [574, 575, 597], "branches": []}
# gained: {"lines": [574, 575, 597], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_nl_365

def test_dcfc_nl_365_no_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = round(dcfc_nl_365(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16986301369863')

def test_dcfc_nl_365_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = round(dcfc_nl_365(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16986301369863')

def test_dcfc_nl_365_full_year():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = round(dcfc_nl_365(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08219178082192')

def test_dcfc_nl_365_more_than_year():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = round(dcfc_nl_365(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.32602739726027')
