# file: pypara/accounting/ledger.py:207-237
# asked: {"lines": [207, 220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [207, 220, 228, 231, 234, 237], "branches": []}

import pytest
from unittest.mock import Mock
from datetime import date
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.ledger import compile_general_ledger_program, ReadInitialBalances, GeneralLedgerProgram, build_general_ledger
from pypara.accounting.journaling import ReadJournalEntries, JournalEntry, Posting
from pypara.accounting.generic import Balance
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Quantity
from decimal import Decimal

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

@pytest.fixture
def mock_read_initial_balances():
    return Mock(spec=ReadInitialBalances)

@pytest.fixture
def mock_read_journal_entries():
    return Mock(spec=ReadJournalEntries)

@pytest.fixture
def mock_build_general_ledger(monkeypatch):
    mock = Mock()
    monkeypatch.setattr('pypara.accounting.ledger.build_general_ledger', mock)
    return mock

def test_compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries, mock_build_general_ledger):
    # Arrange
    period = DateRange(since='2023-01-01', until='2023-12-31')
    mock_account = MockAccount('001', 'Cash', 'Asset', 'Main COA')
    initial_balances = {mock_account: Balance('2023-01-01', Quantity(Decimal('1000.00')))}
    journal_entry = JournalEntry(date=date(2023, 6, 1), description='Test Entry', source=None)
    journal_entries = [journal_entry]
    
    mock_read_initial_balances.return_value = initial_balances
    mock_read_journal_entries.return_value = journal_entries
    
    # Act
    program = compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries)
    general_ledger = program(period)
    
    # Assert
    mock_read_initial_balances.assert_called_once_with(period)
    mock_read_journal_entries.assert_called_once_with(period)
    mock_build_general_ledger.assert_called_once_with(period, journal_entries, initial_balances)
    assert general_ledger == mock_build_general_ledger.return_value
