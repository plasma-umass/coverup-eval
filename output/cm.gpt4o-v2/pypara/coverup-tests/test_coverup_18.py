# file: pypara/accounting/ledger.py:198-204
# asked: {"lines": [198, 199, 203, 204], "branches": []}
# gained: {"lines": [198, 199, 203], "branches": []}

import datetime
from typing import Protocol
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.ledger import GeneralLedgerProgram

class MockGeneralLedger:
    pass

class MockGeneralLedgerProgram:
    def __call__(self, period: DateRange) -> MockGeneralLedger:
        return MockGeneralLedger()

def test_general_ledger_program():
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))
    program = MockGeneralLedgerProgram()
    result = program(period)
    assert isinstance(result, MockGeneralLedger)
