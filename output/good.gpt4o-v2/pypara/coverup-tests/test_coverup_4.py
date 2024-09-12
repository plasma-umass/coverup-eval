# file: pypara/accounting/ledger.py:149-159
# asked: {"lines": [149, 150, 151, 156, 159], "branches": []}
# gained: {"lines": [149, 150, 151, 156, 159], "branches": []}

import pytest
from pypara.accounting.ledger import GeneralLedger, Ledger
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.accounts import Account
from unittest.mock import MagicMock

@pytest.fixture
def mock_date_range():
    return MagicMock(spec=DateRange)

@pytest.fixture
def mock_account():
    return MagicMock(spec=Account)

@pytest.fixture
def mock_ledger(mock_account):
    return Ledger(account=mock_account, initial=MagicMock())

def test_general_ledger_initialization(mock_date_range, mock_account, mock_ledger):
    ledgers = {mock_account: mock_ledger}
    general_ledger = GeneralLedger(period=mock_date_range, ledgers=ledgers)
    
    assert general_ledger.period == mock_date_range
    assert general_ledger.ledgers == ledgers
    assert mock_account in general_ledger.ledgers
    assert general_ledger.ledgers[mock_account] == mock_ledger
