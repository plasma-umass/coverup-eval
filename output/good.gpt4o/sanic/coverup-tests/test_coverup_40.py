# file sanic/router.py:20-28
# lines [20, 21, 26, 27]
# branches []

import pytest
from sanic.router import Router, BaseRouter
from sanic.constants import HTTP_METHODS

def test_router_class_attributes():
    # Ensure Router is a subclass of BaseRouter
    assert issubclass(Router, BaseRouter)
    
    # Ensure DEFAULT_METHOD is set to "GET"
    assert Router.DEFAULT_METHOD == "GET"
    
    # Ensure ALLOWED_METHODS is set to HTTP_METHODS
    assert Router.ALLOWED_METHODS == HTTP_METHODS
