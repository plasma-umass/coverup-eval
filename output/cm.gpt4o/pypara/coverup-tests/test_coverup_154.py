# file pypara/dcc.py:220-237
# lines [225, 228, 229, 231, 234, 237]
# branches ['228->229', '228->231']

import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from pypara.dcc import DCC

@pytest.fixture
def dcc_instance(mocker):
    # Mock the required arguments for DCC
    name = "TestDCC"
    altnames = []
    currencies = []
    calculate_fraction_method = mocker.Mock()
    
    # Create an instance of DCC with mocked arguments
    return DCC(name, altnames, currencies, calculate_fraction_method)

def test_calculate_daily_fraction_edge_case(dcc_instance, mocker):
    start = datetime(2023, 1, 1)
    asof = datetime(2023, 1, 2)
    end = datetime(2023, 12, 31)
    freq = Decimal('1.0')

    # Mock the return values for calculate_fraction_method
    dcc_instance.calculate_fraction_method.side_effect = [Decimal('0.0'), Decimal('0.5')]

    # Test when asof_minus_1 < start
    result = dcc_instance.calculate_daily_fraction(start, asof, end, freq)
    assert result == Decimal('0.5')  # tfact - yfact = 0.5 - 0

    # Test when asof_minus_1 >= start
    asof = datetime(2023, 1, 3)
    dcc_instance.calculate_fraction_method.side_effect = [Decimal('0.5'), Decimal('0.5')]
    result = dcc_instance.calculate_daily_fraction(start, asof, end, freq)
    assert result == Decimal('0.0')  # tfact - yfact = 0.5 - 0.5

    # Clean up mock
    mocker.stopall()
