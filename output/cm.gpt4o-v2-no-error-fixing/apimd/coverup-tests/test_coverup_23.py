# file: apimd/parser.py:259-266
# asked: {"lines": [262, 266], "branches": [[261, 262], [263, 266]]}
# gained: {"lines": [262, 266], "branches": [[261, 262], [263, 266]]}

import pytest
from ast import Attribute, Name, Load
from apimd.parser import Resolver

def test_visit_attribute_not_name():
    resolver = Resolver(root='', alias={})
    node = Attribute(value='not_a_name', attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result == node

def test_visit_attribute_typing():
    resolver = Resolver(root='', alias={})
    node = Attribute(value=Name(id='typing', ctx=Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert isinstance(result, Name)
    assert result.id == 'List'

def test_visit_attribute_other():
    resolver = Resolver(root='', alias={})
    node = Attribute(value=Name(id='other', ctx=Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(node)
    assert result == node
