# file: pypara/accounting/journaling.py:124-129
# asked: {"lines": [129], "branches": []}
# gained: {"lines": [129], "branches": []}

import pytest
from datetime import date
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.commons.numbers import Amount

class MockAccount:
    def __init__(self, name):
        self._name = name

    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return "Asset"

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None

def test_journal_entry_decrements():
    # Setup
    account = MockAccount(name="Cash")
    journal_entry = JournalEntry(date=date.today(), description="Test Entry", source="Test Source")
    posting1 = Posting(journal=journal_entry, date=date.today(), account=account, direction=Direction.DEC, amount=Amount(100))
    posting2 = Posting(journal=journal_entry, date=date.today(), account=account, direction=Direction.INC, amount=Amount(200))
    
    # Add postings to journal entry
    journal_entry.postings.extend([posting1, posting2])
    
    # Test
    decrements = list(journal_entry.decrements)
    assert len(decrements) == 1
    assert decrements[0].direction == Direction.DEC
    assert decrements[0].amount == Amount(100)
    
    # Cleanup
    journal_entry.postings.clear()
