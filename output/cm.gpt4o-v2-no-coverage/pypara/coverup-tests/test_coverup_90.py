# file: pypara/accounting/journaling.py:131-136
# asked: {"lines": [131, 132, 136], "branches": []}
# gained: {"lines": [131, 132, 136], "branches": []}

import pytest
from datetime import date
from dataclasses import dataclass
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Quantity
from pypara.commons.others import Guid

@dataclass(frozen=True)
class MockPosting:
    is_debit: bool

def test_journal_entry_debits():
    # Arrange
    postings = [MockPosting(is_debit=True), MockPosting(is_debit=False), MockPosting(is_debit=True)]
    journal_entry = JournalEntry(date=date.today(), description="Test Entry", source=None)
    object.__setattr__(journal_entry, 'postings', postings)

    # Act
    debits = list(journal_entry.debits)

    # Assert
    assert len(debits) == 2
    assert all(p.is_debit for p in debits)
