# file pypara/dcc.py:443-464
# lines [443, 444, 458, 461, 464]
# branches []

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_act_icma

def _get_actual_day_count(start, end):
    return (end - start).days

@pytest.fixture
def mock_get_actual_day_count(mocker):
    mocker.patch('pypara.dcc._get_actual_day_count', side_effect=_get_actual_day_count)

def test_dcfc_act_act_icma(mock_get_actual_day_count):
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    expected_result = Decimal('0.5245901639')
    
    result = dcfc_act_act_icma(start=start, asof=asof, end=end)
    
    assert round(result, 10) == expected_result
