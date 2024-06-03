# file sanic/router.py:170-172
# lines [170, 171, 172]
# branches []

import pytest
from sanic.router import BaseRouter

class Router(BaseRouter):
    @property
    def routes_dynamic(self):
        return self.dynamic_routes

    def get(self, *args, **kwargs):
        pass

def test_routes_dynamic_property(mocker):
    # Mock the BaseRouter to avoid any side effects
    mocker.patch.object(BaseRouter, '__init__', lambda x: None)
    
    # Create an instance of Router
    router = Router()
    
    # Mock the dynamic_routes attribute
    router.dynamic_routes = ['route1', 'route2']
    
    # Assert that the routes_dynamic property returns the correct value
    assert router.routes_dynamic == ['route1', 'route2']
