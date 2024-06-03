# file pypara/accounting/ledger.py:107-146
# lines [127, 128, 129, 130, 140, 143, 146]
# branches []

import pytest
from datetime import datetime
from pypara.accounting.ledger import Ledger, Account, Balance, LedgerEntry, Posting, Quantity

class MockAccount(Account):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def coa(self):
        return None

    @property
    def code(self):
        return None

    @property
    def parent(self):
        return None

    @property
    def type(self):
        return None

@pytest.fixture
def mock_account():
    return MockAccount(name="Test Account")

@pytest.fixture
def mock_balance():
    return Balance(date=datetime.now(), value=Quantity(100))

@pytest.fixture
def mock_posting():
    class MockPosting:
        def __init__(self, amount, direction):
            self.amount = amount
            self.direction = direction

    class Direction:
        def __init__(self, value):
            self.value = value

    return MockPosting(amount=Quantity(50), direction=Direction(1))

def test_last_balance_with_no_entries(mock_account, mock_balance):
    ledger = Ledger(account=mock_account, initial=mock_balance)
    assert ledger._last_balance == mock_balance.value

def test_add_entry(mock_account, mock_balance, mock_posting):
    ledger = Ledger(account=mock_account, initial=mock_balance)
    entry = ledger.add(mock_posting)
    assert entry in ledger.entries
    assert entry.balance == Quantity(mock_balance.value + mock_posting.amount * mock_posting.direction.value)
