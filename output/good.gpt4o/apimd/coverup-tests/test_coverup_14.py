# file apimd/parser.py:208-217
# lines [208, 210, 211, 212, 213, 214, 215, 217]
# branches ['210->211', '210->212']

import pytest
from unittest.mock import patch
from ast import parse, Constant, Expr, NodeTransformer, AST
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    class TestResolver(Resolver):
        def __init__(self):
            pass
    return TestResolver()

def test_visit_constant_with_non_string(resolver):
    node = Constant(value=123)
    result = resolver.visit_Constant(node)
    assert result == node

def test_visit_constant_with_invalid_syntax(resolver):
    node = Constant(value="invalid syntax")
    with patch('apimd.parser.parse', side_effect=SyntaxError):
        result = resolver.visit_Constant(node)
    assert result == node

def test_visit_constant_with_valid_syntax(resolver):
    node = Constant(value="42")
    result = resolver.visit_Constant(node)
    assert isinstance(result, Constant)
    assert result.value == 42
