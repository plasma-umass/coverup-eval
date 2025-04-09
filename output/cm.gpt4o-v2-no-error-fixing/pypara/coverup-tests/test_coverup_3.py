# file: pypara/accounting/ledger.py:149-159
# asked: {"lines": [149, 150, 151, 156, 159], "branches": []}
# gained: {"lines": [149, 150, 151, 156, 159], "branches": []}

import pytest
from datetime import date
from pypara.accounting.ledger import GeneralLedger
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.accounts import Account
from pypara.accounting.ledger import Ledger
from unittest.mock import Mock

@pytest.fixture
def mock_account():
    return Mock(spec=Account)

@pytest.fixture
def mock_ledger(mock_account):
    return Ledger(account=mock_account, initial=Mock())

@pytest.fixture
def date_range():
    return DateRange(since=date(2023, 1, 1), until=date(2023, 12, 31))

def test_general_ledger_initialization(date_range, mock_ledger, mock_account):
    ledgers = {mock_account: mock_ledger}
    general_ledger = GeneralLedger(period=date_range, ledgers=ledgers)
    
    assert general_ledger.period == date_range
    assert general_ledger.ledgers == ledgers
