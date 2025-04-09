# file sanic/router.py:174-176
# lines [174, 175, 176]
# branches []

import pytest
from sanic.router import BaseRouter

class Router(BaseRouter):
    @property
    def routes_regex(self):
        return self.regex_routes

    def get(self, *args, **kwargs):
        pass

def test_routes_regex_property(mocker):
    # Mock the BaseRouter to avoid any side effects
    mock_base_router = mocker.patch('sanic.router.BaseRouter', autospec=True)
    
    # Create an instance of the Router class
    router = Router()
    
    # Mock the regex_routes attribute
    mock_regex_routes = mocker.PropertyMock(return_value='mocked_regex_routes')
    type(router).regex_routes = mock_regex_routes
    
    # Access the routes_regex property
    result = router.routes_regex
    
    # Assert that the result is as expected
    assert result == 'mocked_regex_routes'
    
    # Assert that the regex_routes property was accessed
    mock_regex_routes.assert_called_once()
