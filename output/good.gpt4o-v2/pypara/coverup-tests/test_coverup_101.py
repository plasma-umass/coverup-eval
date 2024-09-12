# file: pypara/accounting/ledger.py:99-104
# asked: {"lines": [99, 100, 104], "branches": []}
# gained: {"lines": [99, 100, 104], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount

class MockLedger:
    pass

class MockPosting:
    pass

@pytest.fixture
def mock_ledger_entry():
    ledger = MockLedger()
    posting = MockPosting()
    balance = Decimal('100.00')
    return LedgerEntry(ledger=ledger, posting=posting, balance=balance)

def test_credit_property(mock_ledger_entry, monkeypatch):
    def mock_is_credit(self):
        return True

    def mock_amount(self):
        return Amount(Decimal('50.00'))

    monkeypatch.setattr(LedgerEntry, 'is_credit', property(mock_is_credit))
    monkeypatch.setattr(LedgerEntry, 'amount', property(mock_amount))

    assert mock_ledger_entry.credit == Amount(Decimal('50.00'))

    def mock_is_credit_false(self):
        return False

    monkeypatch.setattr(LedgerEntry, 'is_credit', property(mock_is_credit_false))

    assert mock_ledger_entry.credit is None
