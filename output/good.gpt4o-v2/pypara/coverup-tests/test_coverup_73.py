# file: pypara/monetary.py:491-494
# asked: {"lines": [491, 493, 494], "branches": []}
# gained: {"lines": [491, 493, 494], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

def test_scalar_subtract(usd_currency):
    # Setup
    quantity = Decimal("100.00")
    date = Date(2023, 10, 1)
    some_money = SomeMoney(usd_currency, quantity, date)
    
    # Test with int
    result = some_money.scalar_subtract(10)
    assert result.qty == Decimal("90.00").quantize(usd_currency.quantizer)
    
    # Test with float
    result = some_money.scalar_subtract(10.5)
    assert result.qty == Decimal("89.50").quantize(usd_currency.quantizer)
    
    # Test with Decimal
    result = some_money.scalar_subtract(Decimal("10.25"))
    assert result.qty == Decimal("89.75").quantize(usd_currency.quantizer)

    # Test with negative value
    result = some_money.scalar_subtract(-10)
    assert result.qty == Decimal("110.00").quantize(usd_currency.quantizer)
