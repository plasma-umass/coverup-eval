# file: apimd/parser.py:326-339
# asked: {"lines": [], "branches": [[332, 0]]}
# gained: {"lines": [], "branches": [[332, 0]]}

import pytest
from unittest.mock import Mock
from ast import ImportFrom, alias
from apimd.parser import Parser, _m, parent

@pytest.fixture
def parser():
    return Parser()

def test_imports_with_importfrom_node(parser):
    # Create a mock ImportFrom node
    node = Mock(spec=ImportFrom)
    node.module = 'module'
    node.level = 1
    node.names = [alias(name='name', asname=None)]

    # Call the imports method
    parser.imports('root', node)

    # Assert the alias dictionary is updated correctly
    assert parser.alias == {_m('root', 'name'): _m(parent('root', level=0), 'module', 'name')}

def test_imports_with_importfrom_node_no_level(parser):
    # Create a mock ImportFrom node
    node = Mock(spec=ImportFrom)
    node.module = 'module'
    node.level = 0
    node.names = [alias(name='name', asname=None)]

    # Call the imports method
    parser.imports('root', node)

    # Assert the alias dictionary is updated correctly
    assert parser.alias == {_m('root', 'name'): _m('', 'module', 'name')}

def test_imports_with_importfrom_node_no_module(parser):
    # Create a mock ImportFrom node with module set to None
    node = Mock(spec=ImportFrom)
    node.module = None
    node.level = 1
    node.names = [alias(name='name', asname=None)]

    # Call the imports method
    parser.imports('root', node)

    # Assert the alias dictionary is not updated
    assert parser.alias == {}
