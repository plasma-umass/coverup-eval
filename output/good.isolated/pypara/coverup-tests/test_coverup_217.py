# file pypara/dcc.py:220-237
# lines [225, 228, 229, 231, 234, 237]
# branches ['228->229', '228->231']

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import DCC

@pytest.fixture
def mock_calculate_fraction_method(mocker):
    mock = mocker.patch('pypara.dcc.DCC.calculate_fraction_method', return_value=Decimal('0.5'))
    return mock

def test_calculate_daily_fraction(mock_calculate_fraction_method):
    start = datetime.date(2021, 1, 1)
    asof = datetime.date(2021, 1, 3)
    end = datetime.date(2021, 1, 10)
    freq = Decimal('1')

    dcc = DCC('ACT/365', [], [], DCC.calculate_fraction_method)
    result = dcc.calculate_daily_fraction(start, asof, end, freq)

    # Check if the mock method was called correctly for asof_minus_1
    asof_minus_1 = asof - datetime.timedelta(days=1)
    mock_calculate_fraction_method.assert_any_call(start, asof_minus_1, end, freq)

    # Check if the mock method was called correctly for asof
    mock_calculate_fraction_method.assert_any_call(start, asof, end, freq)

    # Check if the result is correct
    assert result == Decimal('0'), "The result should be 0 since mock returns 0.5 for both days"

    # Check if the mock method was called twice
    assert mock_calculate_fraction_method.call_count == 2, "calculate_fraction_method should be called twice"
