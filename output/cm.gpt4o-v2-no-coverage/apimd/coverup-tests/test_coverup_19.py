# file: apimd/parser.py:208-217
# asked: {"lines": [208, 210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}
# gained: {"lines": [208, 210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}

import pytest
from ast import parse, Constant
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root='root', alias={})

def test_visit_constant_with_non_string(resolver):
    node = Constant(value=123)
    result = resolver.visit_Constant(node)
    assert result == node

def test_visit_constant_with_invalid_syntax_string(resolver):
    node = Constant(value="invalid syntax")
    result = resolver.visit_Constant(node)
    assert result == node

def test_visit_constant_with_valid_syntax_string(resolver, mocker):
    node = Constant(value="'valid'")
    mock_visit = mocker.patch.object(resolver, 'visit', return_value='visited')
    result = resolver.visit_Constant(node)
    mock_visit.assert_called_once()
    assert result == 'visited'
