# file: pypara/accounting/ledger.py:64-69
# asked: {"lines": [64, 65, 69], "branches": []}
# gained: {"lines": [64, 65, 69], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.commons.numbers import Amount
from pypara.accounting.accounts import Account
from datetime import date
from unittest.mock import Mock

def test_ledger_entry_amount():
    # Mocking the necessary components
    mock_ledger = Mock()
    mock_account = Mock(spec=Account)
    mock_journal_entry = Mock()
    mock_posting = Posting(
        journal=mock_journal_entry,
        date=date.today(),
        account=mock_account,
        direction=Mock(),
        amount=Amount(Decimal('100.00'))
    )
    mock_quantity = Mock()

    # Creating a LedgerEntry instance
    ledger_entry = LedgerEntry(
        ledger=mock_ledger,
        posting=mock_posting,
        balance=mock_quantity
    )

    # Asserting the amount property
    assert ledger_entry.amount == Amount(Decimal('100.00'))
