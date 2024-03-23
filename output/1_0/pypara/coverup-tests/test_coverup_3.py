# file pypara/accounting/generic.py:13-23
# lines [13, 14, 15, 20, 23]
# branches []

import datetime
from decimal import Decimal
from pypara.accounting.generic import Balance
import pytest

def test_balance_dataclass():
    # Setup
    test_date = datetime.date.today()
    test_value = Decimal('100.00')

    # Exercise
    balance = Balance(date=test_date, value=test_value)

    # Verify
    assert balance.date == test_date
    assert balance.value == test_value

    # Cleanup - not needed here as no external resources or state changes are involved
