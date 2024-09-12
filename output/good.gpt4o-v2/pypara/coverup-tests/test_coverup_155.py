# file: pypara/monetary.py:545-546
# asked: {"lines": [545, 546], "branches": []}
# gained: {"lines": [545, 546], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_with_ccy():
    # Setup initial SomeMoney instance
    original_currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    new_currency = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    some_money = SomeMoney(original_currency, qty, dov)
    
    # Call with_ccy to change the currency
    updated_money = some_money.with_ccy(new_currency)
    
    # Assertions to verify the currency has been updated correctly
    assert updated_money.ccy == new_currency
    assert updated_money.qty == some_money.qty
    assert updated_money.dov == some_money.dov
    assert isinstance(updated_money, SomeMoney)
