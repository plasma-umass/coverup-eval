# file: pypara/accounting/ledger.py:78-83
# asked: {"lines": [78, 79, 83], "branches": []}
# gained: {"lines": [78, 79, 83], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting

class MockPosting:
    def __init__(self, is_debit):
        self.is_debit = is_debit

@pytest.fixture
def mock_posting_debit():
    return MockPosting(is_debit=True)

@pytest.fixture
def mock_posting_credit():
    return MockPosting(is_debit=False)

def test_ledger_entry_is_debit(mock_posting_debit):
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting_debit, balance=None)
    assert ledger_entry.is_debit is True

def test_ledger_entry_is_not_debit(mock_posting_credit):
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting_credit, balance=None)
    assert ledger_entry.is_debit is False
