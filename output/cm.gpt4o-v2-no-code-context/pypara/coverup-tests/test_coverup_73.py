# file: pypara/accounting/journaling.py:138-143
# asked: {"lines": [138, 139, 143], "branches": []}
# gained: {"lines": [138, 139, 143], "branches": []}

import pytest
from pypara.accounting.journaling import JournalEntry, Posting

class TestJournalEntry:
    def test_credits_property(self, mocker):
        # Mock the Posting class
        mock_posting_credit = mocker.Mock(spec=Posting)
        mock_posting_credit.is_credit = True
        
        mock_posting_debit = mocker.Mock(spec=Posting)
        mock_posting_debit.is_credit = False
        
        # Mock the JournalEntry class to include postings
        mock_journal_entry = mocker.Mock(spec=JournalEntry)
        mock_journal_entry.postings = [mock_posting_credit, mock_posting_debit]
        
        # Access the credits property
        credits = list(JournalEntry.credits.__get__(mock_journal_entry))
        
        # Assert that only the credit postings are returned
        assert credits == [mock_posting_credit]
        
        # Clean up
        del mock_journal_entry
        del mock_posting_credit
        del mock_posting_debit
