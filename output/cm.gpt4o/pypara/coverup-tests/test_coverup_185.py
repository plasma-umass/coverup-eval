# file pypara/accounting/ledger.py:78-83
# lines [83]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry

class MockPosting:
    def __init__(self, is_debit):
        self.is_debit = is_debit

class MockLedger:
    pass

def test_ledger_entry_is_debit():
    # Create a mock posting with is_debit set to True
    mock_posting = MockPosting(is_debit=True)
    mock_ledger = MockLedger()
    ledger_entry = LedgerEntry(posting=mock_posting, ledger=mock_ledger, balance=0)
    
    # Assert that is_debit property returns True
    assert ledger_entry.is_debit is True

    # Create a mock posting with is_debit set to False
    mock_posting = MockPosting(is_debit=False)
    ledger_entry = LedgerEntry(posting=mock_posting, ledger=mock_ledger, balance=0)
    
    # Assert that is_debit property returns False
    assert ledger_entry.is_debit is False
