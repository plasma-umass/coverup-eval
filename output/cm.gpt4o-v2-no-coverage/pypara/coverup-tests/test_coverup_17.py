# file: pypara/accounting/ledger.py:107-146
# asked: {"lines": [107, 108, 109, 114, 117, 120, 122, 123, 127, 128, 129, 130, 132, 140, 143, 146], "branches": []}
# gained: {"lines": [107, 108, 109, 114, 117, 120, 122, 123, 127, 128, 129, 130, 132, 140, 143, 146], "branches": []}

import pytest
from unittest.mock import MagicMock
from pypara.accounting.ledger import Ledger
from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Posting, Direction
from pypara.commons.numbers import Quantity

@pytest.fixture
def mock_account():
    return MagicMock(spec=Account)

@pytest.fixture
def mock_balance():
    return MagicMock(spec=Balance)

@pytest.fixture
def mock_posting():
    return MagicMock(spec=Posting)

def test_ledger_initialization(mock_account, mock_balance):
    ledger = Ledger(account=mock_account, initial=mock_balance)
    assert ledger.account == mock_account
    assert ledger.initial == mock_balance
    assert ledger.entries == []

def test_last_balance_with_no_entries(mock_account, mock_balance):
    mock_balance.value = Quantity(100)
    ledger = Ledger(account=mock_account, initial=mock_balance)
    assert ledger._last_balance == Quantity(100)

def test_last_balance_with_entries(mock_account, mock_balance, mock_posting):
    mock_balance.value = Quantity(100)
    ledger = Ledger(account=mock_account, initial=mock_balance)
    mock_entry = MagicMock()
    mock_entry.balance = Quantity(200)
    ledger.entries.append(mock_entry)
    assert ledger._last_balance == Quantity(200)

def test_add_entry(mock_account, mock_balance, mock_posting):
    mock_balance.value = Quantity(100)
    mock_posting.amount = Quantity(50)
    mock_posting.direction = Direction.INC
    ledger = Ledger(account=mock_account, initial=mock_balance)
    
    entry = ledger.add(mock_posting)
    
    assert len(ledger.entries) == 1
    assert ledger.entries[0] == entry
    assert entry.posting == mock_posting
    assert entry.balance == Quantity(150)
