# file: pypara/accounting/journaling.py:60-93
# asked: {"lines": [60, 61, 62, 67, 70, 73, 76, 79, 81, 82, 86, 88, 89, 93], "branches": []}
# gained: {"lines": [60, 61, 62, 67, 70, 73, 76, 79, 81, 82, 86, 88, 89, 93], "branches": []}

import pytest
from datetime import date
from pypara.accounting.journaling import Posting, Direction
from pypara.accounting.accounts import Account, AccountType
from pypara.commons.numbers import Amount

class MockAccount:
    def __init__(self, name, type):
        self._name = name
        self._type = type

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

@pytest.fixture
def sample_account():
    return MockAccount(name="Sample Account", type=AccountType.ASSETS)

@pytest.fixture
def sample_journal_entry():
    return "Sample Journal Entry"

@pytest.fixture
def sample_posting(sample_journal_entry, sample_account):
    return Posting(
        journal=sample_journal_entry,
        date=date.today(),
        account=sample_account,
        direction=Direction.INC,
        amount=Amount(100)
    )

def test_posting_is_debit(sample_posting, monkeypatch):
    def mock_debit_mapping():
        return {Direction.INC: {AccountType.ASSETS, AccountType.EXPENSES}}

    monkeypatch.setattr("pypara.accounting.journaling._debit_mapping", mock_debit_mapping())
    assert sample_posting.is_debit is True

def test_posting_is_credit(sample_posting, monkeypatch):
    def mock_debit_mapping():
        return {Direction.INC: {AccountType.LIABILITIES, AccountType.REVENUES}}

    monkeypatch.setattr("pypara.accounting.journaling._debit_mapping", mock_debit_mapping())
    assert sample_posting.is_credit is True
