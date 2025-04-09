# file pypara/accounting/ledger.py:64-69
# lines [64, 65, 69]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry, Amount

class MockPosting:
    def __init__(self, amount):
        self.amount = amount

class MockLedger:
    pass

class MockBalance:
    pass

def test_ledger_entry_amount():
    mock_posting = MockPosting(Amount(100))
    mock_ledger = MockLedger()
    mock_balance = MockBalance()
    ledger_entry = LedgerEntry(posting=mock_posting, ledger=mock_ledger, balance=mock_balance)
    
    assert ledger_entry.amount == Amount(100)
