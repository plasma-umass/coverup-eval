# file: pypara/accounting/ledger.py:189-195
# asked: {"lines": [189, 190, 194, 195], "branches": []}
# gained: {"lines": [189, 190, 194], "branches": []}

import pytest
import datetime
from typing import Protocol
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.ledger import ReadInitialBalances

class MockInitialBalances:
    pass

class MockReadInitialBalances:
    def __call__(self, period: DateRange) -> MockInitialBalances:
        return MockInitialBalances()

def test_read_initial_balances():
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))
    read_initial_balances = MockReadInitialBalances()
    
    result = read_initial_balances(period)
    
    assert isinstance(result, MockInitialBalances)
