# file pypara/accounting/ledger.py:50-55
# lines [55]
# branches []

import datetime
import pytest
from pypara.accounting.ledger import LedgerEntry

# Assuming that the LedgerEntry class has 'ledger', 'balance', and 'posting' attributes
# and that there is a Posting class defined somewhere in the module with a date attribute.

# Mocking the Posting class for the purpose of this test
class MockPosting:
    def __init__(self, date):
        self.date = date

@pytest.fixture
def mock_posting():
    return MockPosting(datetime.date.today())

@pytest.fixture
def mock_ledger():
    return "mock_ledger"

@pytest.fixture
def mock_balance():
    return 0

def test_ledger_entry_date_property(mock_ledger, mock_balance, mock_posting):
    ledger_entry = LedgerEntry(ledger=mock_ledger, balance=mock_balance, posting=mock_posting)
    assert ledger_entry.date == mock_posting.date, "LedgerEntry date property should return the posting's date"
