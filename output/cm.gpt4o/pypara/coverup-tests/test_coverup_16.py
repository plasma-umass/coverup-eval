# file pypara/accounting/ledger.py:35-49
# lines [35, 36, 37, 42, 45, 48]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry, Ledger, Posting
from decimal import Decimal

class Quantity:
    def __init__(self, amount: Decimal):
        self.amount = amount

@pytest.fixture
def mock_ledger(mocker):
    return mocker.Mock(spec=Ledger)

@pytest.fixture
def mock_posting(mocker):
    return mocker.Mock(spec=Posting)

@pytest.fixture
def mock_quantity():
    return Quantity(amount=Decimal('100.00'))

def test_ledger_entry_initialization(mock_ledger, mock_posting, mock_quantity):
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_quantity)
    
    assert entry.ledger == mock_ledger
    assert entry.posting == mock_posting
    assert entry.balance == mock_quantity
