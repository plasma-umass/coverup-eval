# file pypara/dcc.py:220-237
# lines [229]
# branches ['228->229']

import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from pypara.dcc import DCC

ZERO = Decimal('0.0')

class TestDCC:
    def test_calculate_daily_fraction_asof_minus_1_less_than_start(self, mocker):
        # Mock the calculate_fraction_method to avoid dependency on its implementation
        mocker.patch.object(DCC, 'calculate_fraction_method', return_value=Decimal('0.5'))

        # Create a DCC instance with dummy values for the required fields
        dcc = DCC(name='dummy', altnames=[], currencies=[], calculate_fraction_method=lambda *args: Decimal('0.5'))

        # Define start, asof, and end dates
        start = datetime(2023, 1, 10)
        asof = datetime(2023, 1, 9)
        end = datetime(2023, 12, 31)

        # Call the method under test
        result = dcc.calculate_daily_fraction(start, asof, end)

        # Assert the expected result
        assert result == Decimal('0.5') - ZERO

    def test_calculate_daily_fraction_asof_minus_1_not_less_than_start(self, mocker):
        # Mock the calculate_fraction_method to avoid dependency on its implementation
        mocker.patch.object(DCC, 'calculate_fraction_method', return_value=Decimal('0.5'))

        # Create a DCC instance with dummy values for the required fields
        dcc = DCC(name='dummy', altnames=[], currencies=[], calculate_fraction_method=lambda *args: Decimal('0.5'))

        # Define start, asof, and end dates
        start = datetime(2023, 1, 1)
        asof = datetime(2023, 1, 10)
        end = datetime(2023, 12, 31)

        # Call the method under test
        result = dcc.calculate_daily_fraction(start, asof, end)

        # Assert the expected result
        assert result == Decimal('0.5') - Decimal('0.5')
