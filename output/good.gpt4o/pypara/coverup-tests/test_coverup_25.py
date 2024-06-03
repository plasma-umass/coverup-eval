# file pypara/exchange.py:130-163
# lines [130, 131, 136, 139, 141, 142, 152, 154, 155, 163]
# branches []

import pytest
from unittest.mock import create_autospec
from typing import Optional, Iterable, Tuple
from pypara.exchange import FXRateService, Currency, Date, FXRate

class TestFXRateService:
    def test_query_abstract_method(self):
        # Create a mock subclass of FXRateService
        class MockFXRateService(FXRateService):
            def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
                return None

            def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
                return [None for _ in queries]

        # Instantiate the mock service
        service = MockFXRateService()

        # Create mock parameters
        ccy1 = create_autospec(Currency)
        ccy2 = create_autospec(Currency)
        asof = create_autospec(Date)

        # Call the query method and assert the result
        result = service.query(ccy1, ccy2, asof)
        assert result is None

    def test_queries_abstract_method(self):
        # Create a mock subclass of FXRateService
        class MockFXRateService(FXRateService):
            def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
                return None

            def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
                return [None for _ in queries]

        # Instantiate the mock service
        service = MockFXRateService()

        # Create mock parameters
        ccy1 = create_autospec(Currency)
        ccy2 = create_autospec(Currency)
        asof = create_autospec(Date)
        queries = [(ccy1, ccy2, asof)]

        # Call the queries method and assert the result
        results = list(service.queries(queries))
        assert results == [None]
