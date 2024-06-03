# file sanic/router.py:140-160
# lines [140, 141, 149, 150, 152, 153, 154, 155, 157, 158, 160]
# branches ['149->150', '149->152', '153->154', '153->157', '157->158', '157->160']

import pytest
from sanic.router import Router
from unittest.mock import MagicMock

@pytest.fixture
def mock_app():
    app = MagicMock()
    app._generate_name = MagicMock(side_effect=lambda x: f"generated_{x}")
    return app

@pytest.fixture
def router(mock_app):
    router = Router()
    router.ctx = MagicMock()
    router.ctx.app = mock_app
    router.name_index = {}
    return router

def test_find_route_by_view_name_empty_view_name(router):
    result = router.find_route_by_view_name("")
    assert result is None

def test_find_route_by_view_name_not_in_index(router):
    router.name_index = {}
    result = router.find_route_by_view_name("nonexistent_view")
    assert result is None

def test_find_route_by_view_name_in_index(router):
    mock_route = MagicMock()
    router.name_index = {"existing_view": mock_route}
    result = router.find_route_by_view_name("existing_view")
    assert result == mock_route

def test_find_route_by_view_name_generated_name(router):
    mock_route = MagicMock()
    router.name_index = {"generated_view": mock_route}
    result = router.find_route_by_view_name("view")
    assert result == mock_route

def test_find_route_by_view_name_generated_name_not_found(router):
    router.name_index = {}
    result = router.find_route_by_view_name("view")
    assert result is None
