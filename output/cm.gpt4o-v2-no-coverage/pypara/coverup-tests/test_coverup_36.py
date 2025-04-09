# file: pypara/accounting/ledger.py:189-195
# asked: {"lines": [189, 190, 194, 195], "branches": []}
# gained: {"lines": [189, 190, 194], "branches": []}

import datetime
import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance

def test_read_initial_balances():
    # Create a mock for InitialBalances
    mock_initial_balances = Mock()
    
    # Create a mock for the ReadInitialBalances protocol
    mock_read_initial_balances = Mock(spec=ReadInitialBalances)
    
    # Define a DateRange
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))
    
    # Set the return value of the mock call
    mock_read_initial_balances.return_value = mock_initial_balances
    
    # Call the mock with the period
    result = mock_read_initial_balances(period)
    
    # Assertions
    mock_read_initial_balances.assert_called_once_with(period)
    assert result == mock_initial_balances
