# file sanic/mixins/routes.py:595-620
# lines []
# branches ['617->620']

import pytest
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    def test_generate_name_with_prefix(self, mocker):
        class MockObj:
            def __init__(self, name):
                self.name = name

        mixin = RouteMixin()
        mixin.name = "test_prefix"

        # Mock object with a name that does not start with the prefix
        obj = MockObj("handler_name")
        result = mixin._generate_name(obj)
        assert result == "test_prefix.handler_name"

    def test_generate_name_without_prefix(self, mocker):
        class MockObj:
            def __init__(self, name):
                self.name = name

        mixin = RouteMixin()
        mixin.name = "test_prefix"

        # Mock object with a name that already starts with the prefix
        obj = MockObj("test_prefix.handler_name")
        result = mixin._generate_name(obj)
        assert result == "test_prefix.handler_name"

    def test_generate_name_no_name(self):
        mixin = RouteMixin()
        mixin.name = "test_prefix"

        with pytest.raises(ValueError, match="Could not generate a name for handler"):
            mixin._generate_name(None)
