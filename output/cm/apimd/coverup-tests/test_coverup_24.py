# file apimd/parser.py:259-266
# lines [259, 261, 262, 263, 264, 266]
# branches ['261->262', '261->263', '263->264', '263->266']

import pytest
from apimd.parser import Resolver
from ast import Attribute, Name, Load, parse

class MockRoot:
    pass

@pytest.fixture
def resolver(mocker):
    mocker.patch.object(Resolver, '__init__', return_value=None)
    return Resolver()

def test_visit_attribute_removes_typing_prefix(resolver):
    # Create an Attribute node with 'typing' as the value id
    attribute_node = Attribute(value=Name(id='typing', ctx=Load()), attr='List', ctx=Load())
    # Transform the node
    new_node = resolver.visit_Attribute(attribute_node)
    # Check that the 'typing' prefix was removed
    assert isinstance(new_node, Name)
    assert new_node.id == 'List'

def test_visit_attribute_keeps_non_typing_prefix(resolver):
    # Create an Attribute node with a non-'typing' value id
    attribute_node = Attribute(value=Name(id='other', ctx=Load()), attr='List', ctx=Load())
    # Transform the node
    new_node = resolver.visit_Attribute(attribute_node)
    # Check that the node remains unchanged
    assert isinstance(new_node, Attribute)
    assert new_node.value.id == 'other'
    assert new_node.attr == 'List'

def test_visit_attribute_with_non_name_value(resolver):
    # Create an Attribute node with a non-Name node as value
    attribute_node = Attribute(value=parse('other.get_typing()').body[0].value, attr='List', ctx=Load())
    # Transform the node
    new_node = resolver.visit_Attribute(attribute_node)
    # Check that the node remains unchanged
    assert isinstance(new_node, Attribute)
    assert new_node.attr == 'List'
