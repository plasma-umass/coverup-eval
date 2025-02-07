# file: pypara/accounting/ledger.py:78-83
# asked: {"lines": [78, 79, 83], "branches": []}
# gained: {"lines": [78, 79, 83], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting

class MockPosting:
    def __init__(self, is_debit):
        self.is_debit = is_debit

def test_ledger_entry_is_debit():
    posting = MockPosting(is_debit=True)
    ledger_entry = LedgerEntry(ledger=None, posting=posting, balance=None)
    assert ledger_entry.is_debit is True

def test_ledger_entry_is_not_debit():
    posting = MockPosting(is_debit=False)
    ledger_entry = LedgerEntry(ledger=None, posting=posting, balance=None)
    assert ledger_entry.is_debit is False
