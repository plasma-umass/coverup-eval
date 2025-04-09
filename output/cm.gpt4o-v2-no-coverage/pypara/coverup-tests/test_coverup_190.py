# file: pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from dataclasses import dataclass
from typing import Generic, List, Optional
from pypara.commons.numbers import Amount, Quantity
from pypara.accounting.accounts import Account
from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry, Ledger

def test_ledger_entry_date():
    class MockPosting:
        def __init__(self, date):
            self.date = date

    mock_posting = MockPosting(datetime.date(2023, 1, 1))
    ledger_entry = LedgerEntry(ledger=None, posting=mock_posting, balance=None)
    
    assert ledger_entry.date == datetime.date(2023, 1, 1)
