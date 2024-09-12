# file: pypara/accounting/journaling.py:131-136
# asked: {"lines": [131, 132, 136], "branches": []}
# gained: {"lines": [131, 132, 136], "branches": []}

import datetime
from typing import List, Optional
import pytest
from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.accounts import Account, AccountType, COA
from pypara.commons.numbers import Amount
from pypara.commons.others import Guid

class MockAccount(Account):
    @property
    def code(self):
        return "001"

    @property
    def name(self):
        return "Mock Account"

    @property
    def type(self):
        return AccountType.ASSET

    @property
    def coa(self):
        return COA()

    @property
    def parent(self) -> Optional[Account]:
        return None

class MockPosting(Posting):
    def __init__(self, journal, date, account, direction, amount, is_debit):
        self._is_debit = is_debit
        super().__init__(journal, date, account, direction, amount)

    @property
    def is_debit(self) -> bool:
        return self._is_debit

    @property
    def is_credit(self) -> bool:
        return not self._is_debit

@pytest.fixture
def journal_entry():
    return JournalEntry(
        date=datetime.date.today(),
        description="Test Entry",
        source="Test Source"
    )

def test_debits_property(journal_entry):
    account = MockAccount()
    posting1 = MockPosting(journal_entry, datetime.date.today(), account, "debit", Amount(100), True)
    posting2 = MockPosting(journal_entry, datetime.date.today(), account, "credit", Amount(200), False)
    
    journal_entry.postings.extend([posting1, posting2])
    
    debits = list(journal_entry.debits)
    
    assert len(debits) == 1
    assert debits[0] == posting1
    assert debits[0].is_debit

    # Clean up
    journal_entry.postings.clear()
