# file sanic/mixins/routes.py:349-385
# lines [377, 378, 379, 380, 381, 382, 383, 384]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin

class TestRouteMixin(RouteMixin):
    def route(self, uri, methods, host=None, strict_slashes=None, version=None, name=None, ignore_body=True):
        return {
            "uri": uri,
            "methods": methods,
            "host": host,
            "strict_slashes": strict_slashes,
            "version": version,
            "name": name,
            "ignore_body": ignore_body,
        }

@pytest.fixture
def route_mixin():
    return TestRouteMixin()

def test_options_method(route_mixin):
    uri = "/test"
    host = "127.0.0.1"
    strict_slashes = True
    version = 1
    name = "test_options"
    ignore_body = False

    result = route_mixin.options(
        uri,
        host=host,
        strict_slashes=strict_slashes,
        version=version,
        name=name,
        ignore_body=ignore_body,
    )

    assert result["uri"] == uri
    assert result["methods"] == frozenset({"OPTIONS"})
    assert result["host"] == host
    assert result["strict_slashes"] == strict_slashes
    assert result["version"] == version
    assert result["name"] == name
    assert result["ignore_body"] == ignore_body
