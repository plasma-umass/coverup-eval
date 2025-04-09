# file: pypara/accounting/ledger.py:50-55
# asked: {"lines": [50, 51, 55], "branches": []}
# gained: {"lines": [50, 51, 55], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
import datetime

def test_ledger_entry_date():
    class MockPosting:
        def __init__(self, date):
            self.date = date

    mock_date = datetime.date(2023, 10, 1)
    mock_posting = MockPosting(mock_date)
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting, balance=None)

    assert ledger_entry.date == mock_date
