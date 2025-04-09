# file: pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.accounting.accounts import Account

class MockAccount:
    def __init__(self, code, name, type, coa, parent=None):
        self._code = code
        self._name = name
        self._type = type
        self._coa = coa
        self._parent = parent

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def coa(self):
        return self._coa

    @property
    def parent(self):
        return self._parent

class MockPosting:
    def __init__(self, journal, date, account, direction, amount):
        self.journal = journal
        self.date = date
        self.account = account
        self.direction = direction
        self.amount = amount

    @property
    def is_debit(self):
        return self.direction == 'debit'

    @property
    def is_credit(self):
        return self.direction == 'credit'

class MockJournalEntry:
    def __init__(self, postings):
        self.postings = postings

@pytest.fixture
def mock_ledger_entry():
    account1 = MockAccount('001', 'Cash', 'Asset', 'COA1')
    account2 = MockAccount('002', 'Revenue', 'Income', 'COA1')
    posting1 = MockPosting(None, '2023-01-01', account1, 'debit', 100)
    posting2 = MockPosting(None, '2023-01-01', account2, 'credit', 100)
    journal_entry = MockJournalEntry([posting1, posting2])
    posting1.journal = journal_entry
    posting2.journal = journal_entry
    ledger_entry = LedgerEntry(ledger=None, posting=posting1, balance=100)
    return ledger_entry

def test_cntraccts(mock_ledger_entry):
    cntraccts = mock_ledger_entry.cntraccts
    assert len(cntraccts) == 1
    assert cntraccts[0].name == 'Revenue'
