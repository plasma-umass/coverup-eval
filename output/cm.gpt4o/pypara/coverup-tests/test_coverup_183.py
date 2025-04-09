# file pypara/accounting/ledger.py:85-90
# lines [90]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry

def test_ledger_entry_is_credit():
    # Create a mock posting object with is_credit attribute
    mock_posting = Mock()
    mock_posting.is_credit = True

    # Create a LedgerEntry instance with the mock posting and other required arguments
    ledger_entry = LedgerEntry(ledger=Mock(), balance=Mock(), posting=mock_posting)

    # Assert that the is_credit property returns True
    assert ledger_entry.is_credit == True

    # Clean up
    del ledger_entry
    del mock_posting
