# file: pypara/accounting/ledger.py:92-97
# asked: {"lines": [92, 93, 97], "branches": []}
# gained: {"lines": [92, 93, 97], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount

class MockLedger:
    pass

class MockPosting:
    def __init__(self, amount, is_debit):
        self.amount = amount
        self.is_debit = is_debit

class MockQuantity:
    pass

@pytest.fixture
def mock_ledger_entry():
    ledger = MockLedger()
    posting = MockPosting(amount=Amount(Decimal('100.00')), is_debit=True)
    balance = MockQuantity()
    return LedgerEntry(ledger=ledger, posting=posting, balance=balance)

def test_debit_property(mock_ledger_entry, mocker):
    assert mock_ledger_entry.debit == Amount(Decimal('100.00'))
    
    mock_ledger_entry.posting.is_debit = False
    
    assert mock_ledger_entry.debit is None
