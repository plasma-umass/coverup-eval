# file: pypara/accounting/journaling.py:138-143
# asked: {"lines": [143], "branches": []}
# gained: {"lines": [143], "branches": []}

import datetime
from dataclasses import dataclass, field
from typing import Generic, Iterable, List
from pypara.commons.numbers import Quantity, Amount
from pypara.commons.others import Guid, makeguid
from pypara.accounting.accounts import Account
from pypara.accounting.journaling import JournalEntry, Posting

@dataclass(frozen=True)
class MockAccount:
    name: str

@dataclass(frozen=True)
class MockSource:
    name: str

@dataclass(frozen=True)
class MockPosting:
    journal: JournalEntry
    date: datetime.date
    account: Account
    direction: str
    amount: Amount

    @property
    def is_credit(self) -> bool:
        return self.direction == "credit"

    @property
    def is_debit(self) -> bool:
        return self.direction == "debit"

def test_journal_entry_credits():
    account = MockAccount(name="Cash")
    source = MockSource(name="Test Source")
    postings = [
        MockPosting(journal=None, date=datetime.date.today(), account=account, direction="credit", amount=Amount(100)),
        MockPosting(journal=None, date=datetime.date.today(), account=account, direction="debit", amount=Amount(50)),
    ]
    journal_entry = JournalEntry(date=datetime.date.today(), description="Test Entry", source=source)
    object.__setattr__(journal_entry, 'postings', postings)

    credits = list(journal_entry.credits)
    assert len(credits) == 1
    assert credits[0].direction == "credit"
    assert credits[0].amount == Amount(100)
