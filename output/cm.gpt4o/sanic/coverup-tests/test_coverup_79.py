# file sanic/router.py:166-168
# lines [166, 167, 168]
# branches []

import pytest
from sanic.router import BaseRouter

class Router(BaseRouter):
    @property
    def routes_static(self):
        return self.static_routes

    def get(self, *args, **kwargs):
        pass

def test_routes_static_property(mocker):
    # Mock the BaseRouter to avoid any side effects
    mock_base_router = mocker.patch('sanic.router.BaseRouter', autospec=True)
    
    # Create an instance of Router
    router = Router()
    
    # Mock the static_routes attribute
    mock_static_routes = mocker.PropertyMock(return_value=['/static'])
    type(router).static_routes = mock_static_routes
    
    # Access the routes_static property
    result = router.routes_static
    
    # Assert that the result is as expected
    assert result == ['/static']
    
    # Clean up by deleting the mock
    del type(router).static_routes
