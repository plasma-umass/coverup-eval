# file: pypara/accounting/journaling.py:117-122
# asked: {"lines": [117, 118, 122], "branches": []}
# gained: {"lines": [117, 118, 122], "branches": []}

import datetime
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.accounting.accounts import Account
from pypara.commons.numbers import Amount
import pytest
from unittest.mock import Mock

def test_journal_entry_increments():
    # Setup
    account = Mock(spec=Account)
    journal_entry = JournalEntry(
        date=datetime.date.today(),
        description="Test Entry",
        source="Test Source"
    )
    posting_inc = Posting(
        journal=journal_entry,
        date=datetime.date.today(),
        account=account,
        direction=Direction.INC,
        amount=Amount(100)
    )
    posting_dec = Posting(
        journal=journal_entry,
        date=datetime.date.today(),
        account=account,
        direction=Direction.DEC,
        amount=Amount(50)
    )
    journal_entry.postings.extend([posting_inc, posting_dec])

    # Test
    increments = list(journal_entry.increments)
    assert len(increments) == 1
    assert increments[0].direction == Direction.INC
    assert increments[0].amount == Amount(100)

    # Cleanup
    journal_entry.postings.clear()
