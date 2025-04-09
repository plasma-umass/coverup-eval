# file sanic/mixins/routes.py:527-593
# lines []
# branches ['570->573']

import pytest
from sanic.mixins.routes import RouteMixin
from pathlib import PurePath

class TestRouteMixin:
    @pytest.fixture
    def route_mixin(self):
        class TestClass(RouteMixin):
            def __init__(self):
                self._future_statics = set()
                self.strict_slashes = True

            def _generate_name(self, name):
                return name

            def _apply_static(self, static):
                pass

        return TestClass()

    def test_static_with_invalid_file_or_directory(self, route_mixin):
        with pytest.raises(ValueError) as excinfo:
            route_mixin.static('/test', 12345)  # Invalid type for file_or_directory
        assert "Static route must be a valid path" in str(excinfo.value)

    def test_static_with_strict_slashes(self, route_mixin):
        route_mixin.strict_slashes = True
        route_mixin.static('/test', 'test_directory')
        assert any(static.uri == '/test' for static in route_mixin._future_statics)
        assert any(static.strict_slashes is True for static in route_mixin._future_statics)

    def test_static_with_none_strict_slashes(self, route_mixin):
        route_mixin.strict_slashes = None
        route_mixin.static('/test', 'test_directory', strict_slashes=None)
        assert any(static.uri == '/test' for static in route_mixin._future_statics)
        assert any(static.strict_slashes is None for static in route_mixin._future_statics)
