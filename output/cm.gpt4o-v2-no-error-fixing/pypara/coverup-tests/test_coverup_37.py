# file: pypara/accounting/ledger.py:85-90
# asked: {"lines": [85, 86, 90], "branches": []}
# gained: {"lines": [85, 86, 90], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting

class MockPosting:
    def __init__(self, is_credit):
        self.is_credit = is_credit

def test_ledger_entry_is_credit():
    posting = MockPosting(is_credit=True)
    ledger_entry = LedgerEntry(ledger=None, posting=posting, balance=None)
    assert ledger_entry.is_credit is True

    posting = MockPosting(is_credit=False)
    ledger_entry = LedgerEntry(ledger=None, posting=posting, balance=None)
    assert ledger_entry.is_credit is False
