# file sanic/router.py:47-61
# lines [47, 48, 61]
# branches []

import pytest
from sanic.router import Router, BaseRouter, Route, RouteHandler
from unittest.mock import patch
from typing import Dict, Any, Optional, Tuple

class MockRoute:
    pass

class MockRouteHandler:
    pass

@pytest.fixture
def mock_router():
    class MockRouter(BaseRouter):
        def _get(self, path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
            return MockRoute(), MockRouteHandler(), {"param": "value"}
        
        def get(self, path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
            return self._get(path, method, host)
    
    return MockRouter()

def test_router_get(mock_router):
    router = Router()
    router._get = mock_router._get  # Mock the _get method

    path = "/test"
    method = "GET"
    host = "localhost"

    route, handler, params = router.get(path, method, host)

    assert isinstance(route, MockRoute)
    assert isinstance(handler, MockRouteHandler)
    assert params == {"param": "value"}

    # Ensure the lru_cache is working by calling the method again and checking the cache
    cache_info_before = router.get.cache_info()
    router.get(path, method, host)
    cache_info_after = router.get.cache_info()
    assert cache_info_after.hits == cache_info_before.hits + 1
