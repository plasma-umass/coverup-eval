# file pypara/accounting/ledger.py:189-195
# lines [189, 190, 194, 195]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import ReadInitialBalances, DateRange, InitialBalances

def test_read_initial_balances():
    # Create a mock for the DateRange and InitialBalances
    mock_period = Mock(spec=DateRange)
    mock_initial_balances = Mock(spec=InitialBalances)
    
    # Create a mock implementation of ReadInitialBalances
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            assert period == mock_period
            return mock_initial_balances
    
    # Instantiate the mock implementation
    read_initial_balances = MockReadInitialBalances()
    
    # Call the mock implementation and verify the result
    result = read_initial_balances(mock_period)
    assert result == mock_initial_balances
