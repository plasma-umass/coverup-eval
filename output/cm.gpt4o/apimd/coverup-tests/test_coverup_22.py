# file apimd/parser.py:259-266
# lines [261, 262, 263, 264, 266]
# branches ['261->262', '261->263', '263->264', '263->266']

import pytest
from unittest.mock import MagicMock
from ast import Attribute, Name, Load
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root=None, alias=None)

def test_resolver_visit_attribute_non_name_value(resolver):
    node = Attribute(value=MagicMock(), attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result is node

def test_resolver_visit_attribute_typing(resolver):
    node = Attribute(value=Name(id='typing', ctx=Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert isinstance(result, Name)
    assert result.id == 'List'
    assert isinstance(result.ctx, Load)

def test_resolver_visit_attribute_other(resolver):
    node = Attribute(value=Name(id='other', ctx=Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result is node
