# file sanic/router.py:140-160
# lines [149, 150, 152, 153, 154, 155, 157, 158, 160]
# branches ['149->150', '149->152', '153->154', '153->157', '157->158', '157->160']

import pytest
from sanic.router import Router
from unittest.mock import Mock

@pytest.fixture
def router():
    router = Router()
    router.ctx = Mock()
    router.ctx.app._generate_name = Mock(return_value="generated_name")
    router.name_index = {}
    return router

def test_find_route_by_view_name_empty_view_name(router):
    result = router.find_route_by_view_name("")
    assert result is None

def test_find_route_by_view_name_not_in_index(router):
    router.name_index = {}
    result = router.find_route_by_view_name("non_existent_view")
    assert result is None

def test_find_route_by_view_name_in_index(router):
    mock_route = Mock()
    router.name_index = {"existent_view": mock_route}
    result = router.find_route_by_view_name("existent_view")
    assert result == mock_route

def test_find_route_by_view_name_generated_name(router):
    mock_route = Mock()
    router.name_index = {"generated_name": mock_route}
    result = router.find_route_by_view_name("non_existent_view")
    assert result == mock_route
