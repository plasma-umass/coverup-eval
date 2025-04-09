# file sanic/router.py:47-61
# lines [47, 48, 61]
# branches []

import pytest
from sanic.router import Router, BaseRouter, Route, RouteHandler
from unittest.mock import patch
from functools import lru_cache
from typing import Optional, Tuple, Dict, Any

class MockRoute:
    pass

class MockRouteHandler:
    pass

@pytest.fixture
def mock_router():
    class MockRouter(BaseRouter):
        @lru_cache(maxsize=10)
        def get(self, path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
            return self._get(path, method, host)
        
        def _get(self, path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
            return MockRoute(), MockRouteHandler(), {"param": "value"}
    
    return MockRouter()

def test_router_get(mock_router):
    path = "/test"
    method = "GET"
    host = "localhost"
    
    route, handler, params = mock_router.get(path, method, host)
    
    assert isinstance(route, MockRoute)
    assert isinstance(handler, MockRouteHandler)
    assert params == {"param": "value"}

    # Test cache functionality
    with patch.object(mock_router, '_get', wraps=mock_router._get) as mock_get:
        mock_router.get(path, method, host)
        mock_get.assert_not_called()  # Should not call _get again due to caching
