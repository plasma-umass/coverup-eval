# file pypara/accounting/ledger.py:57-62
# lines [62]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry

def test_ledger_entry_description():
    # Mock the posting and journal objects
    mock_journal = Mock()
    mock_journal.description = "Test Description"
    
    mock_posting = Mock()
    mock_posting.journal = mock_journal
    
    # Mock the ledger and balance objects
    mock_ledger = Mock()
    mock_balance = Mock()
    
    # Create a LedgerEntry instance with the mocked posting, ledger, and balance
    ledger_entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    
    # Assert that the description property returns the correct value
    assert ledger_entry.description == "Test Description"
