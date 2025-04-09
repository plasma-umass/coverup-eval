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
    # Test when posting is credit
    posting_credit = MockPosting(is_credit=True)
    ledger_entry_credit = LedgerEntry(ledger=None, posting=posting_credit, balance=None)
    assert ledger_entry_credit.is_credit is True

    # Test when posting is not credit
    posting_debit = MockPosting(is_credit=False)
    ledger_entry_debit = LedgerEntry(ledger=None, posting=posting_debit, balance=None)
    assert ledger_entry_debit.is_credit is False
