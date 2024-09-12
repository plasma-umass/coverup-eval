# file: pypara/dcc.py:443-464
# asked: {"lines": [443, 444, 458, 461, 464], "branches": []}
# gained: {"lines": [443, 444, 458, 461, 464], "branches": []}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_act_act_icma

def test_dcfc_act_act_icma():
    start = datetime.date(2019, 3, 2)
    asof = datetime.date(2019, 9, 10)
    end = datetime.date(2020, 3, 2)
    result = dcfc_act_act_icma(start=start, asof=asof, end=end)
    assert round(result, 10) == Decimal('0.5245901639')

    # Additional test cases to cover all lines and branches
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 6, 1)
    end = datetime.date(2021, 1, 1)
    result = dcfc_act_act_icma(start=start, asof=asof, end=end)
    assert round(result, 10) == Decimal('0.4153005464')

    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 12, 31)
    end = datetime.date(2021, 1, 1)
    result = dcfc_act_act_icma(start=start, asof=asof, end=end)
    assert round(result, 10) == Decimal('0.9972677596')

    # Test with frequency
    freq = Decimal('2')
    result = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    assert round(result, 10) == Decimal('0.4986338798')
