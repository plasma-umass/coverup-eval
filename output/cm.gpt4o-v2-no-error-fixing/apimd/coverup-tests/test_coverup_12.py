# file: apimd/parser.py:219-234
# asked: {"lines": [219, 221, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 234], "branches": [[221, 222], [221, 223], [224, 225], [224, 234], [227, 228], [227, 232], [230, 231], [230, 232]]}
# gained: {"lines": [219, 221, 222, 223, 224, 225, 227, 232, 234], "branches": [[221, 222], [221, 223], [224, 225], [224, 234], [227, 232]]}

import pytest
from ast import Name, Load
from apimd.parser import Resolver

def _m(root, name):
    return f"{root}.{name}"

@pytest.fixture
def resolver():
    return Resolver(root="root", alias={"root.SomeType": "int", "root.TypeVar": "typing.TypeVar"}, self_ty="self_ty")

def test_visit_name_self_ty(resolver):
    node = Name(id="self_ty", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "Self"

def test_visit_name_in_alias(resolver):
    node = Name(id="SomeType", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "int"

def test_visit_name_typevar(resolver):
    node = Name(id="TypeVar", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "TypeVar"

def test_visit_name_not_in_alias(resolver):
    node = Name(id="OtherType", ctx=Load())
    result = resolver.visit_Name(node)
    assert result == node
