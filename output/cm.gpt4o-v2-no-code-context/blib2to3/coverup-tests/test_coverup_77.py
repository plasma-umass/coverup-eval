# file: src/blib2to3/pgen2/parse.py:226-237
# asked: {"lines": [228, 229, 230, 231, 232, 233, 234, 236, 237], "branches": [[230, 0], [230, 231], [231, 232], [231, 236]]}
# gained: {"lines": [228, 229, 230, 231, 232, 233, 234, 236, 237], "branches": [[230, 231], [231, 232], [231, 236]]}

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

class MockNode:
    def __init__(self):
        self.children = []
        self.used_names = set()

    def append(self, node):
        self.children.append(node)

@pytest.fixture
def parser():
    grammar = Grammar()
    parser = Parser(grammar)
    parser.stack = []
    parser.used_names = set()
    return parser

def test_pop_with_empty_stack(parser):
    # Setup the stack with one element
    parser.stack.append((None, None, [None]))
    parser.convert = lambda grammar, node: MockNode()
    
    # Call the method
    parser.pop()
    
    # Assertions
    assert isinstance(parser.rootnode, MockNode)
    assert parser.rootnode.used_names == parser.used_names

def test_pop_with_non_empty_stack(parser):
    # Setup the stack with two elements
    parser.stack.append((None, None, [MockNode()]))
    parser.stack.append((None, None, [None]))
    parser.convert = lambda grammar, node: MockNode()
    
    # Call the method
    parser.pop()
    
    # Assertions
    assert isinstance(parser.stack[-1][2][-1], MockNode)
