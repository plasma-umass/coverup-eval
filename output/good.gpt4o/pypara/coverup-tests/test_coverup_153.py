# file pypara/monetary.py:555-582
# lines [557, 560, 563, 564, 565, 566, 567, 569, 572, 574, 576, 579, 582]
# branches ['566->567', '566->569', '572->574', '572->582', '574->576', '574->579']

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Currency, FXRateService, Money, NoMoney, ProgrammingError, FXRateLookupError

@pytest.fixture
def mock_fx_rate_service(mocker):
    class MockFXRateService:
        def query(self, from_ccy, to_ccy, asof, strict):
            if from_ccy.code == "USD" and to_ccy.code == "EUR":
                return mocker.Mock(value=Decimal("0.85"))
            return None

    mock_service = MockFXRateService()
    mocker.patch.object(FXRateService, 'default', mock_service)
    return mock_service

@pytest.fixture
def usd_currency():
    return Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def eur_currency():
    return Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def gbp_currency():
    return Currency(code="GBP", name="British Pound", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

def test_convert_success(mock_fx_rate_service, usd_currency, eur_currency):
    money = SomeMoney(usd_currency, Decimal("100.00"), Date(2023, 1, 1))
    converted = money.convert(eur_currency)
    assert converted.ccy == eur_currency
    assert converted.qty == Decimal("85.00")
    assert converted.dov == Date(2023, 1, 1)

def test_convert_no_rate_strict(mock_fx_rate_service, usd_currency, gbp_currency):
    money = SomeMoney(usd_currency, Decimal("100.00"), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        money.convert(gbp_currency, strict=True)

def test_convert_no_rate_non_strict(mock_fx_rate_service, usd_currency, gbp_currency):
    money = SomeMoney(usd_currency, Decimal("100.00"), Date(2023, 1, 1))
    converted = money.convert(gbp_currency, strict=False)
    assert converted == NoMoney

def test_convert_no_fx_service(mocker, usd_currency, eur_currency):
    mocker.patch.object(FXRateService, 'default', None)
    money = SomeMoney(usd_currency, Decimal("100.00"), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        money.convert(eur_currency)
