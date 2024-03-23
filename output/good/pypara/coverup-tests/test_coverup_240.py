# file pypara/dcc.py:220-237
# lines [229]
# branches ['228->229']

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import DCC

@pytest.fixture
def mock_calculate_fraction_method(mocker):
    mock = mocker.patch('pypara.dcc.DCC.calculate_fraction_method', return_value=Decimal('0.5'))
    return mock

def test_calculate_daily_fraction_yfact_zero(mock_calculate_fraction_method):
    start = datetime.date(2021, 1, 2)
    asof = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 1, 3)
    freq = None

    dcc_instance = DCC('name', 'altnames', 'currencies', mock_calculate_fraction_method)
    daily_fraction = dcc_instance.calculate_daily_fraction(start, asof, end, freq)

    mock_calculate_fraction_method.assert_called_once_with(start, asof, end, freq)
    assert daily_fraction == Decimal('0.5'), "The daily fraction should be the result of today's factor since yfact is ZERO"
