# file pypara/accounting/ledger.py:92-97
# lines [92, 93, 97]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry
from decimal import Decimal

class MockLedgerEntry(LedgerEntry):
    def __init__(self, amount, is_debit):
        self._amount = amount
        self._is_debit = is_debit

    @property
    def amount(self):
        return self._amount

    @property
    def is_debit(self):
        return self._is_debit

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Teardown code if necessary

def test_ledger_entry_debit(cleanup):
    # Create a LedgerEntry with is_debit = True
    entry_with_debit = MockLedgerEntry(amount=Decimal('100.00'), is_debit=True)

    # Test that the debit property returns the amount when is_debit is True
    assert entry_with_debit.debit == Decimal('100.00')

    # Create a LedgerEntry with is_debit = False
    entry_without_debit = MockLedgerEntry(amount=Decimal('100.00'), is_debit=False)

    # Test that the debit property returns None when is_debit is False
    assert entry_without_debit.debit is None
