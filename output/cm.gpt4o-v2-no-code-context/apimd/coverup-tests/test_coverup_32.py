# file: apimd/parser.py:259-266
# asked: {"lines": [261, 262, 263, 264, 266], "branches": [[261, 262], [261, 263], [263, 264], [263, 266]]}
# gained: {"lines": [261, 262, 263, 264, 266], "branches": [[261, 262], [261, 263], [263, 264], [263, 266]]}

import pytest
from ast import Attribute, Name, Load
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    class MockResolver(Resolver):
        def __init__(self):
            pass
    return MockResolver()

def test_visit_attribute_with_non_name_value(resolver):
    node = Attribute(value="not_a_name", attr="List", ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result == node

def test_visit_attribute_with_typing_name(resolver):
    node = Attribute(value=Name(id='typing', ctx=Load()), attr="List", ctx=Load())
    result = resolver.visit_Attribute(node)
    assert isinstance(result, Name)
    assert result.id == "List"

def test_visit_attribute_with_non_typing_name(resolver):
    node = Attribute(value=Name(id='not_typing', ctx=Load()), attr="List", ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result == node
