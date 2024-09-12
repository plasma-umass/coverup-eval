# file: pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

import pytest
from decimal import Decimal
from datetime import date
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Amount, Quantity
from unittest.mock import Mock

class MockAccount:
    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return "Mock Account"

    @property
    def type(self):
        return "Asset"

    @property
    def coa(self):
        return "Mock COA"

    @property
    def parent(self):
        return None

class MockLedger:
    def __init__(self):
        self.account = MockAccount()
        self.initial = Mock()

    @property
    def _last_balance(self):
        return Quantity(Decimal('1000.00'))

def test_ledger_entry_amount():
    # Create a mock posting with a specific amount
    mock_posting = Posting(
        journal=Mock(),
        date=date.today(),
        account=MockAccount(),
        direction=Mock(),
        amount=Amount(Decimal('100.00'))
    )
    
    # Create a LedgerEntry instance with the mock posting
    ledger_entry = LedgerEntry(
        ledger=MockLedger(),
        posting=mock_posting,
        balance=Quantity(Decimal('1100.00'))
    )
    
    # Assert that the amount property returns the correct amount
    assert ledger_entry.amount == Amount(Decimal('100.00'))
