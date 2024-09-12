# file: apimd/parser.py:236-257
# asked: {"lines": [239, 244], "branches": [[238, 239], [243, 244]]}
# gained: {"lines": [239, 244], "branches": [[238, 239], [243, 244]]}

import pytest
from ast import Subscript, Name, Load, Tuple, Constant
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root='root', alias={'typing.Union': 'typing.Union'})

def test_visit_subscript_not_name(resolver):
    node = Subscript(value=Constant(value=1), slice=Constant(value=2), ctx=Load())
    result = resolver.visit_Subscript(node)
    assert result == node

def test_visit_subscript_typing_union_not_tuple(resolver, mocker):
    node = Subscript(value=Name(id='typing.Union', ctx=Load()), slice=Constant(value=2), ctx=Load())
    result = resolver.visit_Subscript(node)
    assert result == node.slice
