# file: pypara/dcc.py:443-464
# asked: {"lines": [458, 461, 464], "branches": []}
# gained: {"lines": [458, 461, 464], "branches": []}

import pytest
from decimal import Decimal, InvalidOperation
from datetime import date
from pypara.dcc import dcfc_act_act_icma
from pypara.commons.numbers import ONE

# Mocking _get_actual_day_count since its implementation is not available
def mock_get_actual_day_count(start, end):
    return (end - start).days

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    monkeypatch.setattr('pypara.dcc._get_actual_day_count', mock_get_actual_day_count)

def test_dcfc_act_act_icma_full_coverage():
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    freq = None

    result = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    expected = Decimal('0.5245901639')
    assert round(result, 10) == expected

    # Test with frequency provided
    freq = Decimal('2')
    result_with_freq = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    expected_with_freq = Decimal('0.2622950820')
    assert round(result_with_freq, 10) == expected_with_freq

    # Test with start date equal to asof date
    asof = start
    result_same_start_asof = dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
    expected_same_start_asof = Decimal('0')
    assert result_same_start_asof == expected_same_start_asof

    # Test with start date equal to end date
    end = start
    with pytest.raises(InvalidOperation):
        dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq)
