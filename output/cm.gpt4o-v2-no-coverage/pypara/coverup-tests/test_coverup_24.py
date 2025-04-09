# file: pypara/accounting/journaling.py:174-180
# asked: {"lines": [174, 175, 179, 180], "branches": []}
# gained: {"lines": [174, 175, 179], "branches": []}

import datetime
from typing import Iterable, Protocol
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.journaling import ReadJournalEntries
from pypara.accounting.journaling import JournalEntry

class MockJournalEntry:
    def __init__(self, date, description, source):
        self.date = date
        self.description = description
        self.source = source
        self.postings = []
        self.guid = "mock-guid"

    @property
    def increments(self):
        return []

    @property
    def decrements(self):
        return []

    @property
    def debits(self):
        return []

    @property
    def credits(self):
        return []

    def post(self, date, account, quantity):
        return self

    def validate(self):
        pass

class MockReadJournalEntries:
    def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
        return [MockJournalEntry(datetime.date(2023, 1, 1), "Test Entry", "Test Source")]

def test_read_journal_entries(monkeypatch):
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    reader = MockReadJournalEntries()
    entries = list(reader(period))

    assert len(entries) == 1
    assert entries[0].date == datetime.date(2023, 1, 1)
    assert entries[0].description == "Test Entry"
    assert entries[0].source == "Test Source"
