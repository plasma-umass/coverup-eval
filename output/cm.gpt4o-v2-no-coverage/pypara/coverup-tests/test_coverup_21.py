# file: pypara/accounting/ledger.py:149-159
# asked: {"lines": [149, 150, 151, 156, 159], "branches": []}
# gained: {"lines": [149, 150, 151, 156, 159], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.accounting.ledger import GeneralLedger, Ledger, LedgerEntry
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.accounts import Account
from pypara.accounting.journaling import Posting
from pypara.commons.numbers import Quantity

class MockAccount:
    def __init__(self, code, name, type, coa, parent=None):
        self._code = code
        self._name = name
        self._type = type
        self._coa = coa
        self._parent = parent

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def coa(self):
        return self._coa

    @property
    def parent(self):
        return self._parent

class MockPosting:
    def __init__(self, journal, date, account, direction, amount):
        self.journal = journal
        self.date = date
        self.account = account
        self.direction = direction
        self.amount = amount

    @property
    def is_debit(self):
        return self.direction == "debit"

    @property
    def is_credit(self):
        return self.direction == "credit"

class MockDirection:
    def __init__(self, value):
        self.value = value

class MockBalance:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def mock_account():
    return MockAccount("001", "Cash", "Asset", "Main")

@pytest.fixture
def mock_posting(mock_account):
    return MockPosting("Journal1", date(2023, 1, 1), mock_account, MockDirection(1), Decimal("100.00"))

@pytest.fixture
def mock_ledger(mock_account):
    return Ledger(account=mock_account, initial=MockBalance(Decimal("1000.00")))

def test_general_ledger_initialization(mock_account):
    period = DateRange(date(2023, 1, 1), date(2023, 12, 31))
    ledgers = {mock_account: Ledger(account=mock_account, initial=MockBalance(Decimal("1000.00")))}
    general_ledger = GeneralLedger(period=period, ledgers=ledgers)
    assert general_ledger.period == period
    assert general_ledger.ledgers == ledgers

def test_ledger_add_entry(mock_ledger, mock_posting):
    entry = mock_ledger.add(mock_posting)
    assert entry.posting == mock_posting
    assert entry.balance == Quantity(Decimal("1100.00"))
    assert len(mock_ledger.entries) == 1
    assert mock_ledger.entries[0] == entry

def test_ledger_last_balance(mock_ledger, mock_posting):
    assert mock_ledger._last_balance == Quantity(Decimal("1000.00"))
    mock_ledger.add(mock_posting)
    assert mock_ledger._last_balance == Quantity(Decimal("1100.00"))
