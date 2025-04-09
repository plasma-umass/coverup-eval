# file: pypara/accounting/journaling.py:138-143
# asked: {"lines": [143], "branches": []}
# gained: {"lines": [143], "branches": []}

import datetime
from decimal import Decimal
from typing import Optional
import pytest
from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.accounts import Account, AccountType, COA, Code
from pypara.commons.numbers import Amount

class MockAccount(Account):
    def __init__(self, code, name, account_type, coa, parent=None):
        self._code = code
        self._name = name
        self._type = account_type
        self._coa = coa
        self._parent = parent

    @property
    def code(self) -> Code:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> AccountType:
        return self._type

    @property
    def coa(self) -> COA:
        return self._coa

    @property
    def parent(self) -> Optional[Account]:
        return self._parent

class MockPosting(Posting):
    def __init__(self, journal, date, account, direction, amount, is_credit):
        self._is_credit = is_credit
        super().__init__(journal, date, account, direction, amount)

    @property
    def is_credit(self) -> bool:
        return self._is_credit

@pytest.fixture
def journal_entry():
    return JournalEntry(
        date=datetime.date.today(),
        description="Test Entry",
        source="Test Source"
    )

def test_credits(journal_entry):
    account = MockAccount(code="001", name="Cash", account_type="Asset", coa="Main COA")
    amount = Amount(Decimal('100.0'))
    posting1 = MockPosting(journal_entry, datetime.date.today(), account, "credit", amount, True)
    posting2 = MockPosting(journal_entry, datetime.date.today(), account, "debit", amount, False)
    
    journal_entry.postings.extend([posting1, posting2])
    
    credits = list(journal_entry.credits)
    
    assert len(credits) == 1
    assert credits[0].is_credit
    assert credits[0] == posting1

    # Clean up
    journal_entry.postings.clear()
