# file: pypara/exchange.py:130-163
# asked: {"lines": [130, 131, 136, 139, 141, 142, 152, 154, 155, 163], "branches": []}
# gained: {"lines": [130, 131, 136, 139, 141, 142, 154, 155], "branches": []}

import pytest
from unittest.mock import MagicMock
from typing import Iterable, Optional
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateService

class TestFXRateService(FXRateService):
    def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[float]:
        return 1.25

    def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[float]]:
        return [1.25 for _ in queries]

def test_fx_rate_service_query():
    service = TestFXRateService()
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    asof = Date(2023, 1, 1)
    rate = service.query(ccy1, ccy2, asof)
    assert rate == 1.25

def test_fx_rate_service_queries():
    service = TestFXRateService()
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    asof = Date(2023, 1, 1)
    queries = [(ccy1, ccy2, asof), (ccy2, ccy1, asof)]
    rates = list(service.queries(queries))
    assert rates == [1.25, 1.25]
