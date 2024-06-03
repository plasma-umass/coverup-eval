# file pypara/accounting/ledger.py:50-55
# lines [55]
# branches []

import pytest
from unittest.mock import Mock
from datetime import date
from pypara.accounting.ledger import LedgerEntry

def test_ledger_entry_date():
    # Mock the posting object with a date attribute
    mock_posting = Mock()
    mock_posting.date = date(2023, 10, 1)
    
    # Mock the other required arguments for LedgerEntry
    mock_ledger = Mock()
    mock_balance = Mock()
    
    # Create an instance of LedgerEntry with the mocked arguments
    ledger_entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    
    # Assert that the date property returns the correct date
    assert ledger_entry.date == date(2023, 10, 1)
