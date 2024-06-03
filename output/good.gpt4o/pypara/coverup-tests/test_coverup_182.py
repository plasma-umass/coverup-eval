# file pypara/accounting/journaling.py:138-143
# lines [143]
# branches []

import pytest
from pypara.accounting.journaling import JournalEntry, Posting

def test_journal_entry_credits():
    class MockPosting:
        def __init__(self, is_credit):
            self.is_credit = is_credit

    postings = [MockPosting(True), MockPosting(False), MockPosting(True)]

    class MockJournalEntry(JournalEntry):
        def __init__(self, postings):
            object.__setattr__(self, 'postings', postings)

    journal_entry = MockJournalEntry(postings=postings)

    credits = list(journal_entry.credits)
    
    assert len(credits) == 2
    assert all(p.is_credit for p in credits)
