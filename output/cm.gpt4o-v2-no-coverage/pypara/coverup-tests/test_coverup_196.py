# file: pypara/accounting/journaling.py:124-129
# asked: {"lines": [129], "branches": []}
# gained: {"lines": [129], "branches": []}

import datetime
from typing import List, Optional
import pytest
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.accounting.accounts import Account, AccountType, COA
from pypara.commons.numbers import Amount, Quantity
from pypara.commons.others import Guid, makeguid

class MockAccount:
    def __init__(self, name: str):
        self._name = name

    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return AccountType.ASSET

    @property
    def coa(self):
        return COA(name="Test COA")

    @property
    def parent(self) -> Optional[Account]:
        return None

def test_journal_entry_decrements():
    # Setup
    date = datetime.date.today()
    description = "Test Entry"
    source = "Test Source"
    account = MockAccount(name="Test Account")
    amount = Amount(100)
    posting_dec = Posting(
        journal=None,  # This will be set after JournalEntry creation
        date=date,
        account=account,
        direction=Direction.DEC,
        amount=amount
    )
    posting_inc = Posting(
        journal=None,  # This will be set after JournalEntry creation
        date=date,
        account=account,
        direction=Direction.INC,
        amount=amount
    )
    postings: List[Posting] = [posting_dec, posting_inc]
    
    # Create JournalEntry
    journal_entry = JournalEntry(date=date, description=description, source=source)
    object.__setattr__(journal_entry, 'postings', postings)
    
    # Test decrements property
    decrements = list(journal_entry.decrements)
    assert len(decrements) == 1
    assert decrements[0].direction == Direction.DEC
    assert decrements[0].amount == amount
    assert decrements[0].account == account

    # Clean up
    object.__setattr__(journal_entry, 'postings', [])
