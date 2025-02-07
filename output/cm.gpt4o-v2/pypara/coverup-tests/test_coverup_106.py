# file: pypara/accounting/ledger.py:50-55
# asked: {"lines": [50, 51, 55], "branches": []}
# gained: {"lines": [50, 51, 55], "branches": []}

import pytest
import datetime
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.commons.numbers import Amount, Quantity
from pypara.accounting.accounts import Account

class MockAccount(Account):
    @property
    def code(self):
        return "101"

    @property
    def name(self):
        return "Cash"

    @property
    def type(self):
        return None

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None

def test_ledger_entry_date():
    # Arrange
    mock_ledger = None  # Assuming ledger is not used in the date property
    mock_date = datetime.date(2023, 1, 1)
    mock_posting = Posting(
        journal=None,  # Assuming journal is not used in the date property
        date=mock_date,
        account=MockAccount(),
        direction=None,  # Assuming direction is not used in the date property
        amount=Amount(100)
    )
    ledger_entry = LedgerEntry(
        ledger=mock_ledger,
        posting=mock_posting,
        balance=Quantity(100)
    )

    # Act
    result = ledger_entry.date

    # Assert
    assert result == mock_date
