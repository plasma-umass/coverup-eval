# file: pypara/dcc.py:399-440
# asked: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}
# gained: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_act

def test_dcfc_act_act_non_leap_year(monkeypatch):
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = dcfc_act_act(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16942884946478')

def test_dcfc_act_act_leap_year(monkeypatch):
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = dcfc_act_act(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.17216108990194')

def test_dcfc_act_act_cross_year(monkeypatch):
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = dcfc_act_act(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.08243131970956')

def test_dcfc_act_act_multiple_years(monkeypatch):
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = dcfc_act_act(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.32625945055768')
