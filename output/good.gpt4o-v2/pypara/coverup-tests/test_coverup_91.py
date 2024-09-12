# file: pypara/accounting/ledger.py:71-76
# asked: {"lines": [71, 72, 76], "branches": []}
# gained: {"lines": [71, 72, 76], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.accounting.accounts import Account

def test_cntraccts():
    # Mocking the necessary components
    mock_account = Mock(spec=Account)
    mock_posting = Mock(spec=Posting)
    mock_journal = Mock()
    mock_ledger = Mock()

    # Setting up the mock posting
    mock_posting.direction = 'debit'
    mock_posting.journal = mock_journal

    # Creating mock postings with different directions
    mock_posting1 = Mock(spec=Posting)
    mock_posting1.account = mock_account
    mock_posting1.direction = 'credit'

    mock_posting2 = Mock(spec=Posting)
    mock_posting2.account = mock_account
    mock_posting2.direction = 'debit'

    mock_journal.postings = [mock_posting1, mock_posting2]

    # Creating the LedgerEntry instance
    ledger_entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=Mock())

    # Asserting the cntraccts property
    assert ledger_entry.cntraccts == [mock_account]

    # Clean up
    del ledger_entry
    del mock_posting
    del mock_posting1
    del mock_posting2
    del mock_journal
    del mock_ledger
