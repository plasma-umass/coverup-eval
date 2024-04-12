# file pypara/dcc.py:676-712
# lines [676, 677, 701, 702, 705, 706, 709, 712]
# branches ['701->702', '701->705', '705->706', '705->709']

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_e_plus_360

def test_dcfc_30_e_plus_360_end_of_month():
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = dcfc_30_e_plus_360(start=start, asof=asof, end=end)
    expected = Decimal('0.08611111111111')
    assert round(result, 14) == expected
