# file: pypara/accounting/journaling.py:60-93
# asked: {"lines": [86, 93], "branches": []}
# gained: {"lines": [86, 93], "branches": []}

import datetime
from decimal import Decimal
from typing import List
import pytest
from unittest.mock import Mock
from pypara.commons.numbers import Amount
from pypara.accounting.accounts import Account, AccountType
from pypara.accounting.journaling import Posting, JournalEntry, Direction

class MockAccount:
    def __init__(self, account_type):
        self._type = account_type

    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return "Mock Account"

    @property
    def type(self):
        return self._type

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None

@pytest.fixture
def mock_journal_entry():
    return Mock(spec=JournalEntry)

@pytest.fixture
def mock_account_debit():
    return MockAccount(AccountType.ASSETS)

@pytest.fixture
def mock_account_credit():
    return MockAccount(AccountType.LIABILITIES)

@pytest.fixture
def posting_debit(mock_journal_entry, mock_account_debit):
    return Posting(
        journal=mock_journal_entry,
        date=datetime.date.today(),
        account=mock_account_debit,
        direction=Direction.INC,
        amount=Amount(Decimal('100.00'))
    )

@pytest.fixture
def posting_credit(mock_journal_entry, mock_account_credit):
    return Posting(
        journal=mock_journal_entry,
        date=datetime.date.today(),
        account=mock_account_credit,
        direction=Direction.DEC,
        amount=Amount(Decimal('100.00'))
    )

def test_posting_is_debit(posting_debit):
    assert posting_debit.is_debit
    assert not posting_debit.is_credit

def test_posting_is_credit(posting_credit):
    assert posting_credit.is_credit
    assert not posting_credit.is_debit
