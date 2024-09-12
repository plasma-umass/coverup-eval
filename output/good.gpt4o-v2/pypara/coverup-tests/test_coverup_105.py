# file: pypara/accounting/ledger.py:57-62
# asked: {"lines": [57, 58, 62], "branches": []}
# gained: {"lines": [57, 58, 62], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting

def test_ledger_entry_description():
    # Create a mock journal with a description
    mock_journal = Mock()
    mock_journal.description = "Test Description"
    
    # Create a mock posting with the mock journal
    mock_posting = Mock(spec=Posting)
    mock_posting.journal = mock_journal
    
    # Create a LedgerEntry with the mock posting
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting, balance=None)
    
    # Assert that the description property returns the correct description
    assert ledger_entry.description == "Test Description"
