# file: pypara/accounting/journaling.py:145-158
# asked: {"lines": [156, 157, 158], "branches": [[156, 157], [156, 158]]}
# gained: {"lines": [156, 157, 158], "branches": [[156, 157], [156, 158]]}

import pytest
from unittest.mock import Mock
import datetime
from decimal import Decimal
from pypara.commons.numbers import Amount, Quantity
from pypara.accounting.accounts import Account
from pypara.accounting.journaling import JournalEntry, Posting, Direction

@pytest.fixture
def mock_account():
    account = Mock(spec=Account)
    account.code = "001"
    account.name = "Cash"
    account.type = Mock()
    account.coa = Mock()
    account.parent = None
    return account

@pytest.fixture
def journal_entry():
    return JournalEntry(date=datetime.date.today(), description="Test Entry", source="Test Source")

def test_post_positive_quantity(journal_entry, mock_account):
    date = datetime.date.today()
    quantity = Quantity(Decimal(100))
    journal_entry.post(date, mock_account, quantity)
    assert len(journal_entry.postings) == 1
    posting = journal_entry.postings[0]
    assert posting.journal == journal_entry
    assert posting.date == date
    assert posting.account == mock_account
    assert posting.direction == Direction.INC
    assert posting.amount == Amount(Decimal(100))

def test_post_negative_quantity(journal_entry, mock_account):
    date = datetime.date.today()
    quantity = Quantity(Decimal(-50))
    journal_entry.post(date, mock_account, quantity)
    assert len(journal_entry.postings) == 1
    posting = journal_entry.postings[0]
    assert posting.journal == journal_entry
    assert posting.date == date
    assert posting.account == mock_account
    assert posting.direction == Direction.DEC
    assert posting.amount == Amount(Decimal(50))

def test_post_zero_quantity(journal_entry, mock_account):
    date = datetime.date.today()
    quantity = Quantity(Decimal(0))
    journal_entry.post(date, mock_account, quantity)
    assert len(journal_entry.postings) == 0
