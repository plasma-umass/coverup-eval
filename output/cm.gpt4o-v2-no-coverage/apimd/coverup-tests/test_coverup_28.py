# file: apimd/parser.py:219-234
# asked: {"lines": [222, 225, 227, 228, 229, 230, 231, 232], "branches": [[221, 222], [224, 225], [227, 228], [227, 232], [230, 231], [230, 232]]}
# gained: {"lines": [222, 225, 227, 232], "branches": [[221, 222], [224, 225], [227, 232]]}

import pytest
from ast import parse, Name, Load, Expr, Call, NodeTransformer
from apimd.parser import Resolver

def _m(root, name):
    return f"{root}.{name}"

@pytest.fixture
def resolver():
    return Resolver(root="root", alias={"root.SomeType": "int", "root.TypeVarType": "typing.TypeVar('T')"}, self_ty="self_type")

def test_visit_name_self_type(resolver):
    node = Name(id="self_type", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "Self"

def test_visit_name_alias(resolver):
    node = Name(id="SomeType", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "int"

def test_visit_name_typevar(resolver):
    node = Name(id="TypeVarType", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Call)
    assert isinstance(result.func, Name)
    assert result.func.id == "TypeVar"

def test_visit_name_no_alias(resolver):
    node = Name(id="OtherType", ctx=Load())
    result = resolver.visit_Name(node)
    assert result == node
