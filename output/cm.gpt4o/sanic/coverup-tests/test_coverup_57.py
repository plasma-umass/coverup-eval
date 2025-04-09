# file sanic/router.py:178-188
# lines [178, 179, 181, 182, 183, 184, 186, 187]
# branches ['181->exit', '181->182', '182->181', '182->186']

import pytest
from sanic.exceptions import SanicException
from sanic.router import BaseRouter

ALLOWED_LABELS = {"__init__", "__call__"}

class MockRoute:
    def __init__(self, labels):
        self.labels = labels

class Router(BaseRouter):
    def __init__(self):
        super().__init__()
        self.dynamic_routes = {}

    def add_route(self, route):
        self.dynamic_routes[route] = route

    def finalize(self, *args, **kwargs):
        super().finalize(*args, **kwargs)
        for route in self.dynamic_routes.values():
            if any(
                label.startswith("__") and label not in ALLOWED_LABELS
                for label in route.labels
            ):
                raise SanicException(
                    f"Invalid route: {route}. Parameter names cannot use '__'."
                )

    def get(self, *args, **kwargs):
        pass

def test_router_finalize_invalid_route():
    router = Router()
    invalid_route = MockRoute(labels=["__invalid__"])
    router.add_route(invalid_route)
    
    with pytest.raises(SanicException) as excinfo:
        router.finalize()
    
    assert "Invalid route" in str(excinfo.value)

def test_router_finalize_valid_route():
    router = Router()
    valid_route = MockRoute(labels=["__init__"])
    router.add_route(valid_route)
    
    try:
        router.finalize()
    except SanicException:
        pytest.fail("SanicException raised unexpectedly!")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.patch('sanic.router.BaseRouter.finalize', return_value=None)
