# file pypara/monetary.py:1212-1217
# lines [1213, 1214, 1215, 1216, 1217]
# branches ['1213->1214', '1213->1215', '1215->1216', '1215->1217']

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, IncompatibleCurrencyError
from datetime import date as Date

def test_someprice_lt_undefined_other(mocker):
    # Mocking the other Price object with undefined attribute
    other = mocker.Mock()
    other.undefined = True

    # Creating a mock Currency object
    currency = mocker.Mock(spec=Currency)
    currency.code = "USD"

    some_price = SomePrice(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    
    assert not some_price.lt(other)

def test_someprice_lt_incompatible_currency(mocker):
    # Creating mock Currency objects
    currency_usd = mocker.Mock(spec=Currency)
    currency_usd.code = "USD"
    currency_eur = mocker.Mock(spec=Currency)
    currency_eur.code = "EUR"

    other = SomePrice(ccy=currency_eur, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    some_price = SomePrice(ccy=currency_usd, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        some_price.lt(other)
    
    assert str(excinfo.value) == "USD vs EUR are incompatible for operation '< comparision'."

def test_someprice_lt_comparison(mocker):
    # Creating a mock Currency object
    currency = mocker.Mock(spec=Currency)
    currency.code = "USD"

    other = SomePrice(ccy=currency, qty=Decimal("200.00"), dov=Date(2023, 1, 1))
    some_price = SomePrice(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    
    assert some_price.lt(other)
