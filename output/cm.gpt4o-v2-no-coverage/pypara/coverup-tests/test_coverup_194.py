# file: pypara/accounting/journaling.py:117-122
# asked: {"lines": [122], "branches": []}
# gained: {"lines": [122], "branches": []}

import datetime
from typing import List, Optional
import pytest
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.accounting.accounts import Account, AccountType, COA
from pypara.commons.numbers import Amount, Quantity
from pypara.commons.others import Guid, makeguid

class MockAccount(Account):
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

def test_journal_entry_increments():
    # Setup
    date = datetime.date.today()
    description = "Test Entry"
    source = "Test Source"
    account = MockAccount(name="Test Account")
    postings = [
        Posting(journal=None, date=date, account=account, direction=Direction.INC, amount=Amount(100)),
        Posting(journal=None, date=date, account=account, direction=Direction.DEC, amount=Amount(50)),
    ]
    journal_entry = JournalEntry(date=date, description=description, source=source)
    object.__setattr__(journal_entry, 'postings', postings)

    # Test increments property
    increments = list(journal_entry.increments)
    assert len(increments) == 1
    assert increments[0].direction == Direction.INC

    # Cleanup
    del journal_entry
    del postings

@pytest.fixture
def mock_postings():
    date = datetime.date.today()
    account = MockAccount(name="Mock Account")
    postings = [
        Posting(journal=None, date=date, account=account, direction=Direction.INC, amount=Amount(100)),
        Posting(journal=None, date=date, account=account, direction=Direction.DEC, amount=Amount(50)),
    ]
    return postings

def test_journal_entry_increments_with_fixture(mock_postings):
    # Setup
    date = datetime.date.today()
    description = "Test Entry"
    source = "Test Source"
    journal_entry = JournalEntry(date=date, description=description, source=source)
    object.__setattr__(journal_entry, 'postings', mock_postings)

    # Test increments property
    increments = list(journal_entry.increments)
    assert len(increments) == 1
    assert increments[0].direction == Direction.INC

    # Cleanup
    del journal_entry
