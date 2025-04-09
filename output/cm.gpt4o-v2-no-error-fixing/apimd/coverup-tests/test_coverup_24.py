# file: apimd/parser.py:208-217
# asked: {"lines": [210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}
# gained: {"lines": [210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}

import pytest
from ast import Constant, Expr, Name
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root="", alias={})

def test_visit_constant_non_string(resolver):
    node = Constant(value=123)
    result = resolver.visit_Constant(node)
    assert result is node

def test_visit_constant_syntax_error(resolver, mocker):
    node = Constant(value="invalid syntax")
    mocker.patch("apimd.parser.parse", side_effect=SyntaxError)
    result = resolver.visit_Constant(node)
    assert result is node

def test_visit_constant_valid_string(resolver, mocker):
    node = Constant(value="valid_name")
    expr = Expr(value=Name(id="valid_name", ctx=None))
    mocker.patch("apimd.parser.parse", return_value=Expr(body=[expr]))
    mock_visit = mocker.patch.object(resolver, 'visit', return_value=Name(id="valid_name", ctx=None))
    result = resolver.visit_Constant(node)
    mock_visit.assert_called_once_with(expr.value)
    assert isinstance(result, Name)
    assert result.id == "valid_name"
