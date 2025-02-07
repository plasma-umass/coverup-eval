# file: pypara/monetary.py:555-582
# asked: {"lines": [555, 557, 560, 563, 564, 565, 566, 567, 569, 572, 574, 576, 579, 582], "branches": [[566, 567], [566, 569], [572, 574], [572, 582], [574, 576], [574, 579]]}
# gained: {"lines": [555, 557, 560, 563, 564, 565, 566, 567, 572, 574, 576, 579, 582], "branches": [[566, 567], [572, 574], [572, 582], [574, 576], [574, 579]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, NoMoney
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateService, FXRateLookupError
from pypara.commons.errors import ProgrammingError
from pypara.commons.zeitgeist import Date

class MockFXRateService(FXRateService):
    def query(self, ccy1, ccy2, asof, strict=False):
        if ccy1.code == "USD" and ccy2.code == "EUR":
            return MockFXRate(Decimal("0.85"))
        return None

    def queries(self, queries, strict=False):
        return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

class MockFXRate:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def setup_fxrate_service(monkeypatch):
    monkeypatch.setattr(FXRateService, 'default', MockFXRateService())

def test_convert_success(setup_fxrate_service):
    usd = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    money = SomeMoney(usd, Decimal("100.00"), Date.today())
    converted = money.convert(eur)
    assert converted.ccy == eur
    assert converted.qty == Decimal("85.00")

def test_convert_no_fxrate_service():
    usd = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    money = SomeMoney(usd, Decimal("100.00"), Date.today())
    FXRateService.default = None
    with pytest.raises(ProgrammingError):
        money.convert(eur)

def test_convert_fxrate_not_found_strict(setup_fxrate_service):
    usd = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    jpy = Currency.of("JPY", "Japanese Yen", 0, CurrencyType.MONEY)
    money = SomeMoney(usd, Decimal("100.00"), Date.today())
    with pytest.raises(FXRateLookupError):
        money.convert(jpy, strict=True)

def test_convert_fxrate_not_found_non_strict(setup_fxrate_service):
    usd = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    jpy = Currency.of("JPY", "Japanese Yen", 0, CurrencyType.MONEY)
    money = SomeMoney(usd, Decimal("100.00"), Date.today())
    converted = money.convert(jpy, strict=False)
    assert converted == NoMoney
