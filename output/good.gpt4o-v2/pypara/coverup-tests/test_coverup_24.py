# file: pypara/monetary.py:313-320
# asked: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}
# gained: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}

import pytest
from decimal import Decimal
from pypara.monetary import Money, SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_money_of_with_none_values():
    assert Money.of(None, None, None) is Money.NA

def test_money_of_with_valid_values():
    ccy = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    qty = Decimal('100.00')
    dov = Date(2023, 10, 1)
    result = Money.of(ccy, qty, dov)
    assert isinstance(result, SomeMoney)
    assert result.ccy == ccy
    assert result.qty == ccy.quantize(qty)
    assert result.dov == dov
