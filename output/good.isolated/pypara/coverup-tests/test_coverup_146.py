# file pypara/accounting/ledger.py:85-90
# lines [85, 86, 90]
# branches []

import pytest
from pypara.accounting.ledger import LedgerEntry
from typing import TypeVar

_T = TypeVar('_T')

# Mock class for Posting to be used in the tests
class MockPosting:
    def __init__(self, is_credit):
        self._is_credit = is_credit

    @property
    def is_credit(self):
        return self._is_credit

@pytest.fixture
def mock_posting(mocker):
    # Create a mock Posting object
    return MockPosting(is_credit=True)

def test_ledger_entry_is_credit():
    # Set up the mock to return True for is_credit
    mock_posting_true = MockPosting(is_credit=True)
    ledger_entry_true = LedgerEntry(posting=mock_posting_true, ledger=None, balance=None)
    assert ledger_entry_true.is_credit == True

    # Set up the mock to return False for is_credit
    mock_posting_false = MockPosting(is_credit=False)
    ledger_entry_false = LedgerEntry(posting=mock_posting_false, ledger=None, balance=None)
    assert ledger_entry_false.is_credit == False
