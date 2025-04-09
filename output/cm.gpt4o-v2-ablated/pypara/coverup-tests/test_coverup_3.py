# file: pypara/dcc.py:443-464
# asked: {"lines": [443, 444, 458, 461, 464], "branches": []}
# gained: {"lines": [443, 444, 458, 461, 464], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_act_icma

def _get_actual_day_count(start, end):
    return (end - start).days

@pytest.fixture
def mock_get_actual_day_count(monkeypatch):
    monkeypatch.setattr('pypara.dcc._get_actual_day_count', _get_actual_day_count)

def test_dcfc_act_act_icma_full_coverage(mock_get_actual_day_count):
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    freq = Decimal('1')
    
    result = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    assert round(result, 10) == Decimal('0.5245901639')
    
    # Test with freq as None
    result = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=None)
    assert round(result, 10) == Decimal('0.5245901639')
    
    # Test with different dates
    start = date(2020, 1, 1)
    asof = date(2020, 6, 1)
    end = date(2021, 1, 1)
    result = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    expected_result = Decimal(_get_actual_day_count(start, asof)) / Decimal(_get_actual_day_count(start, end)) / freq
    assert result == expected_result
