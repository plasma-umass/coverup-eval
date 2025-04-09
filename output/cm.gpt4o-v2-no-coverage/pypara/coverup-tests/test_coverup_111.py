# file: pypara/accounting/ledger.py:99-104
# asked: {"lines": [99, 100, 104], "branches": []}
# gained: {"lines": [99, 100, 104], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount, Quantity

class MockPosting:
    def __init__(self, amount, is_credit):
        self.amount = amount
        self.is_credit = is_credit

class MockLedger:
    pass

@pytest.fixture
def mock_posting():
    return MockPosting(amount=Amount(Decimal('100.00')), is_credit=True)

@pytest.fixture
def mock_ledger():
    return MockLedger()

@pytest.fixture
def mock_quantity():
    return Quantity(Decimal('100.00'))

def test_ledger_entry_credit(mock_ledger, mock_posting, mock_quantity):
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_quantity)
    assert entry.credit == Amount(Decimal('100.00'))

def test_ledger_entry_no_credit(mock_ledger, mock_posting, mock_quantity):
    mock_posting.is_credit = False
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_quantity)
    assert entry.credit is None
