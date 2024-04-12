# file pypara/monetary.py:1249-1276
# lines [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276]
# branches ['1260->1261', '1260->1263', '1266->1268', '1266->1276', '1268->1270', '1268->1273']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, Currency, Price, FXRateService, ProgrammingError, FXRateLookupError, NoPrice

class MockFXRateService:
    def query(self, from_currency, to_currency, asof, strict):
        if from_currency.code == "USD" and to_currency.code == "EUR":
            return type('FXRate', (object,), {'value': Decimal('0.85')})
        return None

@pytest.fixture
def mock_fx_rate_service(mocker):
    service = MockFXRateService()
    mocker.patch.object(FXRateService, 'default', new=service)
    return service

def test_convert_with_valid_rate(mock_fx_rate_service):
    usd_currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    eur_currency = Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    price = SomePrice(usd_currency, Decimal('100'), date.today())
    converted_price = price.convert(eur_currency)
    assert converted_price.ccy == eur_currency
    assert converted_price.qty == Decimal('85')
    assert converted_price.dov == date.today()

def test_convert_with_no_default_service_raises_programming_error(mocker):
    usd_currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    mocker.patch.object(FXRateService, 'default', new=None)
    price = SomePrice(usd_currency, Decimal('100'), date.today())
    with pytest.raises(ProgrammingError):
        price.convert(usd_currency)

def test_convert_with_no_rate_and_strict_raises_fxratelookuperror(mock_fx_rate_service):
    usd_currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    gbp_currency = Currency(code="GBP", name="British Pound", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    price = SomePrice(usd_currency, Decimal('100'), date.today())
    with pytest.raises(FXRateLookupError):
        price.convert(gbp_currency, strict=True)

def test_convert_with_no_rate_and_not_strict_returns_noprice(mock_fx_rate_service):
    usd_currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    gbp_currency = Currency(code="GBP", name="British Pound", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)
    price = SomePrice(usd_currency, Decimal('100'), date.today())
    converted_price = price.convert(gbp_currency, strict=False)
    assert converted_price == NoPrice
