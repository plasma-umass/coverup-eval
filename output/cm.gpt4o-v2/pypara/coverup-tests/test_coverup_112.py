# file: pypara/accounting/ledger.py:92-97
# asked: {"lines": [92, 93, 97], "branches": []}
# gained: {"lines": [92, 93, 97], "branches": []}

import pytest
from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting
from pypara.commons.numbers import Amount, Quantity
from unittest.mock import Mock, PropertyMock

@pytest.fixture
def mock_ledger():
    return Mock()

@pytest.fixture
def mock_posting():
    return Mock()

@pytest.fixture
def ledger_entry(mock_ledger, mock_posting):
    return LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=Quantity(0))

def test_debit_property_debit(ledger_entry, mocker):
    mocker.patch.object(type(ledger_entry), 'is_debit', new_callable=PropertyMock, return_value=True)
    mocker.patch.object(type(ledger_entry), 'amount', new_callable=PropertyMock, return_value=Amount(100))
    assert ledger_entry.debit == Amount(100)

def test_debit_property_not_debit(ledger_entry, mocker):
    mocker.patch.object(type(ledger_entry), 'is_debit', new_callable=PropertyMock, return_value=False)
    assert ledger_entry.debit is None
