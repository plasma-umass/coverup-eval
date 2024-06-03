# file pypara/accounting/journaling.py:117-122
# lines [122]
# branches []

import pytest
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from datetime import datetime

def test_journal_entry_increments():
    # Create mock postings
    posting_inc = Posting(journal="TestJournal", date=datetime.now(), account="TestAccount", direction=Direction.INC, amount=100)
    posting_dec = Posting(journal="TestJournal", date=datetime.now(), account="TestAccount", direction=Direction.DEC, amount=50)
    
    # Create a JournalEntry with the mock postings
    class TestJournalEntry(JournalEntry):
        def __init__(self, postings):
            object.__setattr__(self, 'postings', postings)
    
    journal_entry = TestJournalEntry(postings=[posting_inc, posting_dec])
    
    # Get increments
    increments = list(journal_entry.increments)
    
    # Assertions to verify the increments
    assert len(increments) == 1
    assert increments[0] == posting_inc

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Code to cleanup after tests
