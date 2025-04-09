# file sanic/mixins/middleware.py:8-9
# lines [8, 9]
# branches []

import pytest
from sanic.mixins.middleware import MiddlewareMixin

def test_middleware_mixin_initialization():
    # Create an instance of MiddlewareMixin
    middleware_mixin = MiddlewareMixin()
    
    # Assert that the _future_middleware attribute is initialized correctly
    assert isinstance(middleware_mixin._future_middleware, list)
    assert len(middleware_mixin._future_middleware) == 0
