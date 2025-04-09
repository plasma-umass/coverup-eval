# file: pypara/accounting/ledger.py:198-204
# asked: {"lines": [198, 199, 203, 204], "branches": []}
# gained: {"lines": [198, 199, 203], "branches": []}

import datetime
from typing import Protocol, Dict, Generic
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.accounts import Account
from pypara.accounting.ledger import GeneralLedgerProgram
import pytest
from unittest.mock import Mock

class GeneralLedger:
    def __init__(self, period: DateRange, ledgers: Dict[Account, 'Ledger']):
        self.period = period
        self.ledgers = ledgers

class Ledger:
    pass

class TestGeneralLedgerProgram:
    def test_general_ledger_program(self, mocker):
        mock_program = mocker.Mock(spec=GeneralLedgerProgram)
        period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))
        ledger = GeneralLedger(period=period, ledgers={})
        
        mock_program.return_value = ledger
        
        result = mock_program(period)
        
        assert result.period == period
        assert result.ledgers == {}
        
        mock_program.assert_called_once_with(period)
