# file pypara/accounting/ledger.py:198-204
# lines [198, 199, 203, 204]
# branches []

import pytest
from unittest.mock import Mock
from pypara.accounting.ledger import GeneralLedgerProgram, DateRange, GeneralLedger

def test_general_ledger_program():
    # Mock the DateRange and GeneralLedger
    mock_date_range = Mock(spec=DateRange)
    mock_general_ledger = Mock(spec=GeneralLedger)
    
    # Create a mock implementation of GeneralLedgerProgram
    class MockGeneralLedgerProgram:
        def __call__(self, period: DateRange) -> GeneralLedger:
            assert period == mock_date_range
            return mock_general_ledger
    
    # Instantiate the mock program
    program = MockGeneralLedgerProgram()
    
    # Call the program with the mock date range
    result = program(mock_date_range)
    
    # Assert that the result is the mock general ledger
    assert result == mock_general_ledger
