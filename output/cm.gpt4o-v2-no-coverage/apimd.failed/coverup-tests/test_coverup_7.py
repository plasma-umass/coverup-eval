# file: apimd/parser.py:208-217
# asked: {"lines": [208, 210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}
# gained: {"lines": [208, 210, 211, 212, 213, 214, 215, 217], "branches": [[210, 211], [210, 212]]}

import pytest
from ast import Constant, Name
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root="", alias={})

def test_visit_constant_with_non_string(resolver):
    node = Constant(value=123)
    result = resolver.visit_Constant(node)
    assert result is node

def test_visit_constant_with_invalid_syntax(resolver):
    node = Constant(value="invalid syntax @")
    result = resolver.visit_Constant(node)
    assert result is node

def test_visit_constant_with_valid_string(resolver, mocker):
    node = Constant(value="valid_name")
    mock_visit = mocker.patch.object(resolver, 'visit', return_value=Name(id='valid_name'))
    result = resolver.visit_Constant(node)
    mock_visit.assert_called_once()
    assert isinstance(result, Name)
    assert result.id == 'valid_name'
