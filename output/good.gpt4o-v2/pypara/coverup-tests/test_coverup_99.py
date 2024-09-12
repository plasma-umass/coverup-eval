# file: pypara/accounting/journaling.py:138-143
# asked: {"lines": [138, 139, 143], "branches": []}
# gained: {"lines": [138, 139, 143], "branches": []}

import datetime
from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.accounts import Account, AccountType, COA
from pypara.commons.numbers import Amount

def test_journal_entry_credits():
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
        def parent(self):
            return None

    class MockSource:
        pass

    class MockPosting(Posting):
        @property
        def is_credit(self) -> bool:
            return True

    date = datetime.date.today()
    description = "Test Entry"
    source = MockSource()
    account = MockAccount()
    amount = Amount(100)

    posting1 = MockPosting(journal=None, date=date, account=account, direction=None, amount=amount)
    posting2 = MockPosting(journal=None, date=date, account=account, direction=None, amount=amount)

    journal_entry = JournalEntry(date=date, description=description, source=source)
    journal_entry.postings.extend([posting1, posting2])

    credits = list(journal_entry.credits)
    assert len(credits) == 2
    assert all(p.is_credit for p in credits)
