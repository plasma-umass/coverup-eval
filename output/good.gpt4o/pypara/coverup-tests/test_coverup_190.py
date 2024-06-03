# file pypara/accounting/journaling.py:124-129
# lines [129]
# branches []

import pytest
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from datetime import date

def test_journal_entry_decrements():
    # Create mock postings
    posting1 = Posting(journal="journal1", date=date.today(), account="account1", direction=Direction.DEC, amount=100)
    posting2 = Posting(journal="journal2", date=date.today(), account="account2", direction=Direction.INC, amount=200)
    posting3 = Posting(journal="journal3", date=date.today(), account="account3", direction=Direction.DEC, amount=300)
    
    # Create a mock JournalEntry class to include postings
    class MockJournalEntry(JournalEntry):
        def __init__(self, postings):
            object.__setattr__(self, 'postings', postings)
    
    # Create a JournalEntry with the mock postings
    journal_entry = MockJournalEntry(postings=[posting1, posting2, posting3])
    
    # Get the decrements
    decrements = list(journal_entry.decrements)
    
    # Assertions to verify the correct postings are returned
    assert len(decrements) == 2
    assert decrements[0] == posting1
    assert decrements[1] == posting3
