# file: src/blib2to3/pgen2/parse.py:219-224
# asked: {"lines": [219, 221, 222, 223, 224], "branches": []}
# gained: {"lines": [219, 221, 222, 223, 224], "branches": []}

import pytest
from blib2to3.pytree import Context, RawNode
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar
from unittest.mock import MagicMock

@pytest.fixture
def parser():
    grammar = Grammar()
    return Parser(grammar)

def test_push(parser):
    # Mocking the stack and its elements
    mock_dfa = MagicMock()
    mock_state = 1
    mock_node = MagicMock()
    parser.stack = [(mock_dfa, mock_state, mock_node)]
    
    # Mocking newdfa and newstate
    newdfa = MagicMock()
    newstate = 2
    
    # Creating a context
    context = ("test", (1, 2))
    
    # Expected newnode
    expected_newnode = (999, None, context, [])
    
    # Call the method
    parser.push(999, newdfa, newstate, context)
    
    # Assertions
    assert parser.stack[-2] == (mock_dfa, newstate, mock_node)
    assert parser.stack[-1] == (newdfa, 0, expected_newnode)
