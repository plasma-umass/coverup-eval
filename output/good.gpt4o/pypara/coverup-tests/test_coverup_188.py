# file pypara/accounting/journaling.py:174-180
# lines [180]
# branches []

import pytest
from pypara.accounting.journaling import ReadJournalEntries, DateRange, JournalEntry
from typing import Iterable

class MockJournalEntry:
    pass

class MockReadJournalEntries(ReadJournalEntries[MockJournalEntry]):
    def __call__(self, period: DateRange) -> Iterable[JournalEntry[MockJournalEntry]]:
        return [MockJournalEntry()]

def test_read_journal_entries():
    period = DateRange("2023-01-01", "2023-12-31")
    reader = MockReadJournalEntries()
    entries = list(reader(period))
    
    assert len(entries) == 1
    assert isinstance(entries[0], MockJournalEntry)

def test_protocol_unimplemented():
    class UnimplementedReadJournalEntries(ReadJournalEntries[MockJournalEntry]):
        pass

    period = DateRange("2023-01-01", "2023-12-31")
    reader = UnimplementedReadJournalEntries()
    
    with pytest.raises(TypeError):
        list(reader(period))
