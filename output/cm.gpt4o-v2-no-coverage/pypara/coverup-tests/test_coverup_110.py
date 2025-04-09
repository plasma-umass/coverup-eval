# file: pypara/accounting/ledger.py:71-76
# asked: {"lines": [71, 72, 76], "branches": []}
# gained: {"lines": [71, 72, 76], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.accounts import Account
from pypara.accounting.journaling import Posting

class MockJournal:
    def __init__(self, postings):
        self.postings = postings

@pytest.fixture
def mock_posting():
    journal = MockJournal([])
    posting = Mock(spec=Posting)
    posting.journal = journal
    return posting

def test_cntraccts(mock_posting):
    account1 = Mock(spec=Account)
    account2 = Mock(spec=Account)
    posting1 = Mock(spec=Posting)
    posting2 = Mock(spec=Posting)
    
    posting1.account = account1
    posting1.direction = 'debit'
    posting2.account = account2
    posting2.direction = 'credit'
    
    mock_posting.journal.postings = [posting1, posting2]
    mock_posting.direction = 'debit'
    
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting, balance=None)
    
    cntraccts = ledger_entry.cntraccts
    
    assert cntraccts == [account2]

    mock_posting.direction = 'credit'
    
    cntraccts = ledger_entry.cntraccts
    
    assert cntraccts == [account1]
