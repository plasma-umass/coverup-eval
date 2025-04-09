# file pypara/accounting/ledger.py:189-195
# lines [189, 190, 194, 195]
# branches []

import pytest
from pypara.accounting.ledger import ReadInitialBalances
from datetime import date
from typing import NamedTuple

# Assuming DateRange and InitialBalances are defined somewhere in the module
# If not, we need to define them for the test to work
class DateRange(NamedTuple):
    start: date
    end: date

class InitialBalances(NamedTuple):
    balances: dict

# Mocking the ReadInitialBalances protocol
class MockReadInitialBalances(ReadInitialBalances):
    def __call__(self, period: DateRange) -> InitialBalances:
        return InitialBalances(balances={'account1': 1000, 'account2': 2000})

@pytest.fixture
def mock_read_initial_balances():
    return MockReadInitialBalances()

def test_read_initial_balances_protocol(mock_read_initial_balances):
    period = DateRange(start=date(2021, 1, 1), end=date(2021, 12, 31))
    initial_balances = mock_read_initial_balances(period)
    assert isinstance(initial_balances, InitialBalances)
    assert initial_balances.balances == {'account1': 1000, 'account2': 2000}
