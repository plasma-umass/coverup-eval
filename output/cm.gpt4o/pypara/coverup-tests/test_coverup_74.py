# file pypara/accounting/ledger.py:92-97
# lines [92, 93, 97]
# branches []

import pytest
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from pypara.accounting.ledger import Amount

_T = TypeVar('_T')

@dataclass
class LedgerEntry(Generic[_T]):
    amount: _T
    is_debit: bool

    @property
    def debit(self) -> Optional[Amount]:
        """
        Returns the debit amount, if any.
        """
        return self.amount if self.is_debit else None

@pytest.fixture
def mock_amount(mocker):
    return mocker.Mock(spec=Amount)

def test_ledger_entry_debit_is_debit(mock_amount):
    entry = LedgerEntry(amount=mock_amount, is_debit=True)
    assert entry.debit == mock_amount

def test_ledger_entry_debit_is_not_debit(mock_amount):
    entry = LedgerEntry(amount=mock_amount, is_debit=False)
    assert entry.debit is None
