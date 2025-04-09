# file: pypara/accounting/ledger.py:64-69
# asked: {"lines": [64, 65, 69], "branches": []}
# gained: {"lines": [64, 65, 69], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry, Amount

class MockPosting:
    def __init__(self, amount):
        self.amount = amount

class MockLedger:
    pass

@pytest.fixture
def ledger_entry():
    posting = MockPosting(Amount(100))
    ledger = MockLedger()
    balance = Amount(0)
    return LedgerEntry(ledger=ledger, posting=posting, balance=balance)

def test_ledger_entry_amount(ledger_entry):
    assert ledger_entry.amount == Amount(100)
