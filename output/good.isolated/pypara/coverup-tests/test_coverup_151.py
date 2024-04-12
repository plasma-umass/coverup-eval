# file pypara/accounting/ledger.py:78-83
# lines [78, 79, 83]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry
from typing import Generic, TypeVar

_T = TypeVar('_T')

class MockPosting(Generic[_T]):
    def __init__(self, is_debit):
        self._is_debit = is_debit

    @property
    def is_debit(self):
        return self._is_debit

@pytest.fixture
def mock_posting_debit():
    return MockPosting(is_debit=True)

@pytest.fixture
def mock_posting_credit():
    return MockPosting(is_debit=False)

def test_ledger_entry_is_debit(mock_posting_debit):
    entry = LedgerEntry(ledger='ledger', balance=100, posting=mock_posting_debit)
    assert entry.is_debit == True

def test_ledger_entry_is_not_debit(mock_posting_credit):
    entry = LedgerEntry(ledger='ledger', balance=100, posting=mock_posting_credit)
    assert entry.is_debit == False
