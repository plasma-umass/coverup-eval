# file: pypara/accounting/ledger.py:64-69
# asked: {"lines": [64, 65, 69], "branches": []}
# gained: {"lines": [64, 65, 69], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.commons.numbers import Amount
from pypara.accounting.accounts import Account

class MockPosting:
    def __init__(self, amount):
        self.amount = amount

class MockLedger:
    pass

def test_ledger_entry_amount():
    mock_posting = MockPosting(Amount(Decimal('100.00')))
    ledger_entry = LedgerEntry(ledger=MockLedger(), posting=mock_posting, balance=Decimal('0.00'))
    
    assert ledger_entry.amount == Amount(Decimal('100.00'))

