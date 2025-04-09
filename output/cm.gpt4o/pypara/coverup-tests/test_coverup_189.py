# file pypara/accounting/ledger.py:71-76
# lines [76]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry, Account

def test_ledger_entry_cntraccts():
    # Mocking the necessary objects and their attributes
    mock_account1 = Mock(spec=Account)
    mock_account2 = Mock(spec=Account)
    
    mock_posting1 = Mock()
    mock_posting1.account = mock_account1
    mock_posting1.direction = 'debit'
    
    mock_posting2 = Mock()
    mock_posting2.account = mock_account2
    mock_posting2.direction = 'credit'
    
    mock_journal = Mock()
    mock_journal.postings = [mock_posting1, mock_posting2]
    
    mock_posting = Mock()
    mock_posting.journal = mock_journal
    mock_posting.direction = 'debit'
    
    mock_ledger = Mock()
    mock_balance = Mock()
    
    ledger_entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    
    # Execute the method to cover line 76
    cntraccts = ledger_entry.cntraccts
    
    # Assertions to verify the postconditions
    assert len(cntraccts) == 1
    assert cntraccts[0] == mock_account2
