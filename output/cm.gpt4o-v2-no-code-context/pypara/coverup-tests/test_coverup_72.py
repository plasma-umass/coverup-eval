# file: pypara/accounting/journaling.py:124-129
# asked: {"lines": [124, 125, 129], "branches": []}
# gained: {"lines": [124, 125, 129], "branches": []}

import pytest
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from datetime import datetime
from typing import List

def test_journal_entry_decrements():
    # Create mock postings
    posting1 = Posting(journal="journal1", date=datetime.now(), account="account1", direction=Direction.DEC, amount=100)
    posting2 = Posting(journal="journal2", date=datetime.now(), account="account2", direction=Direction.INC, amount=200)
    posting3 = Posting(journal="journal3", date=datetime.now(), account="account3", direction=Direction.DEC, amount=300)

    # Create a subclass of JournalEntry to add postings attribute
    class TestJournalEntry(JournalEntry):
        def __init__(self, postings: List[Posting]):
            object.__setattr__(self, 'postings', postings)

    # Create a TestJournalEntry with the mock postings
    journal_entry = TestJournalEntry(postings=[posting1, posting2, posting3])

    # Get the decrements
    decrements = list(journal_entry.decrements)

    # Assertions to verify the correct postings are returned
    assert len(decrements) == 2
    assert decrements[0] == posting1
    assert decrements[1] == posting3

    # Clean up
    del journal_entry
    del posting1
    del posting2
    del posting3
    del decrements
