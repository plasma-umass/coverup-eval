# file pypara/accounting/ledger.py:35-49
# lines [35, 36, 37, 42, 45, 48]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry
from unittest.mock import MagicMock

# Assuming the existence of the Ledger class and Quantity class
# Since Posting class does not exist, we will mock it.

class MockLedger:
    pass

@pytest.fixture
def mock_ledger():
    return MockLedger()

@pytest.fixture
def mock_posting():
    return MagicMock()

@pytest.fixture
def mock_balance():
    return MagicMock()

def test_ledger_entry_initialization(mock_ledger, mock_posting, mock_balance):
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    assert entry.ledger == mock_ledger
    assert entry.posting == mock_posting
    assert entry.balance == mock_balance
