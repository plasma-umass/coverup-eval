# file: pypara/accounting/journaling.py:174-180
# asked: {"lines": [174, 175, 179, 180], "branches": []}
# gained: {"lines": [174, 175, 179], "branches": []}

import pytest
from typing import Iterable
from datetime import date
from pypara.accounting.journaling import ReadJournalEntries
from pypara.commons.zeitgeist import DateRange

class MockJournalEntry:
    pass

class MockReadJournalEntries:
    def __call__(self, period: DateRange) -> Iterable[MockJournalEntry]:
        return [MockJournalEntry()]

def test_read_journal_entries():
    period = DateRange(since=date(2023, 1, 1), until=date(2023, 12, 31))
    reader = MockReadJournalEntries()
    entries = list(reader(period))
    
    assert len(entries) > 0
    assert isinstance(entries[0], MockJournalEntry)
