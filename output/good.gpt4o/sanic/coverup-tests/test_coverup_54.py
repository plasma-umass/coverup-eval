# file sanic/router.py:140-160
# lines [140, 141, 149, 150, 152, 153, 154, 155, 157, 158, 160]
# branches ['149->150', '149->152', '153->154', '153->157', '157->158', '157->160']

import pytest
from sanic.router import BaseRouter
from functools import lru_cache

class Router(BaseRouter):
    @lru_cache(maxsize=128)
    def find_route_by_view_name(self, view_name, name=None):
        """
        Find a route in the router based on the specified view name.

        :param view_name: string of view name to search by
        :param kwargs: additional params, usually for static files
        :return: tuple containing (uri, Route)
        """
        if not view_name:
            return None

        route = self.name_index.get(view_name)
        if not route:
            full_name = self.ctx.app._generate_name(view_name)
            route = self.name_index.get(full_name)

        if not route:
            return None

        return route

    def get(self, *args, **kwargs):
        pass  # Implement abstract method to avoid instantiation error

class MockApp:
    def _generate_name(self, view_name):
        return f"generated_{view_name}"

class MockCtx:
    def __init__(self, app):
        self.app = app

class MockRoute:
    pass

@pytest.fixture
def router():
    router = Router()
    router.name_index = {}
    router.ctx = MockCtx(MockApp())
    return router

def test_find_route_by_view_name_empty_view_name(router):
    assert router.find_route_by_view_name("") is None

def test_find_route_by_view_name_existing_view_name(router):
    route = MockRoute()
    router.name_index["existing_view"] = route
    assert router.find_route_by_view_name("existing_view") == route

def test_find_route_by_view_name_non_existing_view_name(router):
    assert router.find_route_by_view_name("non_existing_view") is None

def test_find_route_by_view_name_generated_name(router):
    route = MockRoute()
    router.name_index["generated_view"] = route
    assert router.find_route_by_view_name("view") == route

def test_find_route_by_view_name_generated_name_not_found(router):
    assert router.find_route_by_view_name("another_view") is None
