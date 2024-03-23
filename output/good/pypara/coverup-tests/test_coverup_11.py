# file pypara/dcc.py:443-464
# lines [443, 444, 458, 461, 464]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.dcc import dcfc_act_act_icma

@pytest.fixture
def mock_get_actual_day_count(mocker):
    mocker.patch('pypara.dcc._get_actual_day_count', side_effect=lambda start, end: (end - start).days)

def test_dcfc_act_act_icma_with_freq(mock_get_actual_day_count):
    start = date(2020, 1, 1)
    asof = date(2020, 6, 1)
    end = date(2021, 1, 1)
    freq = Decimal('2')
    
    result = dcfc_act_act_icma(start, asof, end, freq)
    
    expected_p1 = Decimal((asof - start).days)
    expected_p2 = Decimal((end - start).days)
    expected_result = expected_p1 / expected_p2 / freq
    
    assert result == expected_result, "The day count fraction calculated is incorrect"
