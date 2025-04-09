# file pypara/accounting/ledger.py:207-237
# lines [207, 220, 228, 231, 234, 237]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import compile_general_ledger_program

# Mocking the DateRange and GeneralLedger classes since they are not available
class DateRange:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

class GeneralLedger:
    def __init__(self, entries, balances):
        self.entries = entries
        self.balances = balances

@pytest.fixture
def mock_read_initial_balances():
    return Mock()

@pytest.fixture
def mock_read_journal_entries():
    return Mock()

@pytest.fixture
def mock_build_general_ledger(mocker):
    return mocker.patch('pypara.accounting.ledger.build_general_ledger')

def test_compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries, mock_build_general_ledger):
    # Arrange
    period = DateRange(start_date='2023-01-01', end_date='2023-12-31')
    initial_balances = {'account1': 1000, 'account2': 2000}
    journal_entries = [{'entry1': 'data1'}, {'entry2': 'data2'}]
    expected_ledger = GeneralLedger(entries=journal_entries, balances=initial_balances)

    mock_read_initial_balances.return_value = initial_balances
    mock_read_journal_entries.return_value = journal_entries
    mock_build_general_ledger.return_value = expected_ledger

    # Act
    general_ledger_program = compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries)
    result = general_ledger_program(period)

    # Assert
    mock_read_initial_balances.assert_called_once_with(period)
    mock_read_journal_entries.assert_called_once_with(period)
    mock_build_general_ledger.assert_called_once_with(period, journal_entries, initial_balances)
    assert result == expected_ledger
