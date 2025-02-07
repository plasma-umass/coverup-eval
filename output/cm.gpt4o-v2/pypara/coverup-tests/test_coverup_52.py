# file: pypara/accounting/ledger.py:107-146
# asked: {"lines": [107, 108, 109, 114, 117, 120, 122, 123, 127, 128, 129, 130, 132, 140, 143, 146], "branches": []}
# gained: {"lines": [107, 108, 109, 114, 117, 120, 122, 123, 127, 128, 129, 130, 132, 140, 143, 146], "branches": []}

import pytest
from pypara.accounting.ledger import Ledger
from pypara.accounting.journaling import Posting
from pypara.accounting.generic import Balance
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Quantity, Amount
from datetime import date
from unittest.mock import Mock

class MockAccount(Account):
    def __init__(self, name):
        self._name = name

    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return Mock()

    @property
    def coa(self):
        return Mock()

    @property
    def parent(self):
        return None

@pytest.fixture
def account():
    return MockAccount(name="Cash")

@pytest.fixture
def initial_balance():
    return Balance(date=date.today(), value=Quantity(1000))

@pytest.fixture
def ledger(account, initial_balance):
    return Ledger(account=account, initial=initial_balance)

@pytest.fixture
def posting(account):
    journal_entry = Mock()
    return Posting(
        journal=journal_entry,
        date=date.today(),
        account=account,
        direction=Mock(value=1),  # Assuming 1 represents a positive direction
        amount=Amount(100)
    )

def test_last_balance_with_no_entries(ledger):
    assert ledger._last_balance == Quantity(1000)

def test_last_balance_with_entries(ledger, posting):
    ledger.add(posting)
    assert ledger._last_balance == Quantity(1100)

def test_add_entry(ledger, posting):
    entry = ledger.add(posting)
    assert entry.posting == posting
    assert entry.balance == Quantity(1100)
    assert ledger.entries[-1] == entry

def test_add_multiple_entries(ledger, posting):
    posting2 = Posting(
        journal=posting.journal,
        date=date.today(),
        account=posting.account,
        direction=Mock(value=-1),  # Assuming -1 represents a negative direction
        amount=Amount(200)
    )
    ledger.add(posting)
    ledger.add(posting2)
    assert ledger._last_balance == Quantity(900)
    assert len(ledger.entries) == 2
    assert ledger.entries[0].balance == Quantity(1100)
    assert ledger.entries[1].balance == Quantity(900)
