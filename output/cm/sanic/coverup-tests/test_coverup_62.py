# file sanic/mixins/routes.py:595-620
# lines [595, 596, 598, 599, 600, 601, 602, 604, 605, 606, 607, 608, 609, 610, 612, 614, 615, 617, 618, 620]
# branches ['598->599', '598->614', '599->598', '599->600', '600->601', '600->604', '614->615', '614->617', '617->618', '617->620']

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.exceptions import SanicException
from uuid import uuid4

class NamedObject:
    def __init__(self, name):
        self.name = name

class UnnamedObject:
    pass

@pytest.fixture
def route_mixin():
    app_name = f"TestApp_{uuid4()}"
    app = Sanic(app_name)
    mixin = RouteMixin()
    mixin.name = app_name  # Set the name attribute to mimic the app's name
    yield mixin
    del app

def test_generate_name_with_string(route_mixin):
    name = route_mixin._generate_name("test_string")
    assert name == f"{route_mixin.name}.test_string"

def test_generate_name_with_named_object(route_mixin):
    named_obj = NamedObject("test_named_object")
    name = route_mixin._generate_name(named_obj)
    assert name == f"{route_mixin.name}.test_named_object"

def test_generate_name_with_unnamed_object(route_mixin):
    unnamed_obj = UnnamedObject()
    with pytest.raises(ValueError):
        route_mixin._generate_name(unnamed_obj)

def test_generate_name_with_lambda(route_mixin):
    lambda_func = lambda x: x  # noqa: E731
    lambda_func.__name__ = "test_lambda"
    name = route_mixin._generate_name(lambda_func)
    assert name == f"{route_mixin.name}.test_lambda"

def test_generate_name_with_none(route_mixin):
    with pytest.raises(ValueError):
        route_mixin._generate_name(None)

def test_generate_name_with_multiple_objects(route_mixin):
    named_obj = NamedObject("test_named_object")
    unnamed_obj = UnnamedObject()
    name = route_mixin._generate_name(unnamed_obj, named_obj)
    assert name == f"{route_mixin.name}.test_named_object"

def test_generate_name_with_multiple_strings(route_mixin):
    name = route_mixin._generate_name("first_string", "second_string")
    assert name == f"{route_mixin.name}.first_string"

def test_generate_name_with_mixed_objects(route_mixin):
    named_obj = NamedObject("test_named_object")
    unnamed_obj = UnnamedObject()
    name = route_mixin._generate_name("test_string", unnamed_obj, named_obj)
    assert name == f"{route_mixin.name}.test_string"
