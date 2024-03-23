# file sanic/mixins/routes.py:595-620
# lines []
# branches ['617->620']

import pytest
from sanic.mixins.routes import RouteMixin

class MockClassWithName:
    name = "mock_class_name"

class MockClassWithDunderName:
    __name__ = "mock_dunder_name"

class MockClassWithoutName:
    pass

class MockRouteMixin(RouteMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

@pytest.fixture
def route_mixin():
    return MockRouteMixin(name="mixin")

def test_generate_name_with_object_having_name_attribute(route_mixin):
    name = route_mixin._generate_name(MockClassWithName())
    assert name == "mixin.mock_class_name"

def test_generate_name_with_object_having_dunder_name_attribute(route_mixin):
    name = route_mixin._generate_name(MockClassWithDunderName())
    assert name == "mixin.mock_dunder_name"

def test_generate_name_with_object_having_no_name_attribute(route_mixin):
    with pytest.raises(ValueError):
        route_mixin._generate_name(MockClassWithoutName())

def test_generate_name_with_prefix_not_matching_mixin_name(route_mixin):
    name = route_mixin._generate_name("handler")
    assert name == "mixin.handler"

def test_generate_name_with_prefix_already_matching_mixin_name(route_mixin):
    name = route_mixin._generate_name("mixin.handler")
    assert name == "mixin.handler"
