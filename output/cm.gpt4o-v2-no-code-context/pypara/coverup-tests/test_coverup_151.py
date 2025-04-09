# file: pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry, Account

class MockAccount(Account):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def coa(self):
        return None

    @property
    def code(self):
        return None

    @property
    def parent(self):
        return None

    @property
    def type(self):
        return None

@pytest.fixture
def mock_posting():
    mock_posting = Mock()
    mock_posting.direction = 'debit'
    return mock_posting

@pytest.fixture
def mock_journal():
    mock_journal = Mock()
    return mock_journal

@pytest.fixture
def mock_postings(mock_posting):
    mock_posting1 = Mock()
    mock_posting1.direction = 'credit'
    mock_posting1.account = MockAccount(name='Account1')

    mock_posting2 = Mock()
    mock_posting2.direction = 'debit'
    mock_posting2.account = MockAccount(name='Account2')

    mock_posting3 = Mock()
    mock_posting3.direction = 'credit'
    mock_posting3.account = MockAccount(name='Account3')

    return [mock_posting1, mock_posting2, mock_posting3]

@pytest.fixture
def ledger_entry(mock_posting, mock_journal, mock_postings):
    mock_journal.postings = mock_postings
    mock_posting.journal = mock_journal
    ledger = Mock()
    balance = Mock()
    entry = LedgerEntry(ledger=ledger, posting=mock_posting, balance=balance)
    return entry

def test_cntraccts(ledger_entry):
    cntraccts = ledger_entry.cntraccts
    assert len(cntraccts) == 2
    assert cntraccts[0].name == 'Account1'
    assert cntraccts[1].name == 'Account3'
