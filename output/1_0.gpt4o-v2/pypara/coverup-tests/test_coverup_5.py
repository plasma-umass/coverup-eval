# file: pypara/accounting/generic.py:13-23
# asked: {"lines": [13, 14, 15, 20, 23], "branches": []}
# gained: {"lines": [13, 14, 15, 20, 23], "branches": []}

import pytest
from datetime import date, timedelta
from decimal import Decimal
from pypara.accounting.generic import Balance
from pypara.commons.numbers import Quantity
from dataclasses import FrozenInstanceError

def test_balance_creation():
    balance_date = date.today()
    balance_value = Quantity(Decimal('100.00'))
    balance = Balance(date=balance_date, value=balance_value)
    
    assert balance.date == balance_date
    assert balance.value == balance_value

def test_balance_immutability():
    balance_date = date.today()
    balance_value = Quantity(Decimal('100.00'))
    balance = Balance(date=balance_date, value=balance_value)
    
    with pytest.raises(FrozenInstanceError):
        balance.date = balance_date + timedelta(days=1)
    
    with pytest.raises(FrozenInstanceError):
        balance.value = Quantity(Decimal('200.00'))
