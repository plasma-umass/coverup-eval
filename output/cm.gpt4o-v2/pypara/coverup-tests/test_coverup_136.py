# file: pypara/accounting/ledger.py:85-90
# asked: {"lines": [85, 86, 90], "branches": []}
# gained: {"lines": [85, 86, 90], "branches": []}

import pytest
from unittest.mock import Mock, PropertyMock
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Amount
from datetime import date

@pytest.fixture
def sample_account():
    account = Mock(spec=Account)
    account.name = "Sample Account"
    account.code = "001"
    account.type = "Asset"  # Assuming "Asset" is a valid type; replace with actual enum if needed
    account.coa = None  # Assuming None for simplicity; replace with actual COA if needed
    account.parent = None
    return account

@pytest.fixture
def sample_posting(sample_account):
    amount = Amount(100)
    posting = Mock(spec=Posting)
    posting.journal = None  # Assuming None for simplicity; replace with actual JournalEntry if needed
    posting.date = date.today()
    posting.account = sample_account
    posting.direction = "credit"  # Assuming "credit" is a valid direction; replace with actual enum if needed
    posting.amount = amount
    return posting

@pytest.fixture
def sample_ledger_entry(sample_posting):
    ledger = None  # Assuming None for simplicity; replace with actual Ledger if needed
    balance = 100  # Assuming a simple balance; replace with actual Quantity if needed
    return LedgerEntry(ledger=ledger, posting=sample_posting, balance=balance)

def test_is_credit(sample_ledger_entry, sample_posting):
    # Mock the is_credit property of Posting
    type(sample_posting).is_credit = PropertyMock(return_value=True)
    assert sample_ledger_entry.is_credit is True

    type(sample_posting).is_credit = PropertyMock(return_value=False)
    assert sample_ledger_entry.is_credit is False
