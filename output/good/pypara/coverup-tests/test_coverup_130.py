# file pypara/accounting/ledger.py:57-62
# lines [57, 58, 62]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry
from unittest.mock import MagicMock

@pytest.fixture
def mock_journal():
    mock = MagicMock()
    mock.description = "Test Journal Description"
    return mock

@pytest.fixture
def mock_posting(mock_journal):
    mock = MagicMock()
    mock.journal = mock_journal
    return mock

@pytest.fixture
def mock_ledger():
    return MagicMock()

@pytest.fixture
def mock_balance():
    return MagicMock()

def test_ledger_entry_description(mock_posting, mock_ledger, mock_balance):
    ledger_entry = LedgerEntry(posting=mock_posting, ledger=mock_ledger, balance=mock_balance)
    assert ledger_entry.description == "Test Journal Description"
