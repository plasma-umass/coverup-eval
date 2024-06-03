# file sanic/router.py:178-188
# lines [179, 181, 182, 183, 184, 186, 187]
# branches ['181->exit', '181->182', '182->181', '182->186']

import pytest
from sanic.exceptions import SanicException
from sanic.router import Router, BaseRouter

class MockRoute:
    def __init__(self, labels):
        self.labels = labels

    def __repr__(self):
        return f"<MockRoute object at {id(self)}>"

@pytest.fixture
def mock_router(mocker):
    class MockRouter(Router):
        def __init__(self):
            super().__init__()
            self.dynamic_routes = {}

    mock_router = MockRouter()
    mocker.patch.object(BaseRouter, 'finalize', return_value=None)
    return mock_router

def test_finalize_invalid_route(mock_router):
    # Add a route with invalid labels
    route = MockRoute(labels=['__invalid'])
    mock_router.dynamic_routes['/invalid'] = route

    with pytest.raises(SanicException) as excinfo:
        mock_router.finalize()

    assert str(excinfo.value) == f"Invalid route: {route}. Parameter names cannot use '__'."

def test_finalize_valid_route(mock_router):
    # Add a route with valid labels
    mock_router.dynamic_routes['/valid'] = MockRoute(labels=['valid'])

    # This should not raise an exception
    mock_router.finalize()
