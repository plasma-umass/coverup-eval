# file: src/blib2to3/pgen2/parse.py:226-237
# asked: {"lines": [226, 228, 229, 230, 231, 232, 233, 234, 236, 237], "branches": [[230, 0], [230, 231], [231, 232], [231, 236]]}
# gained: {"lines": [226, 228, 229, 230, 231, 232, 233, 234, 236, 237], "branches": [[230, 231], [231, 232], [231, 236]]}

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

class MockGrammar(Grammar):
    pass

class MockNode:
    def __init__(self):
        self.used_names = set()
    def append(self, node):
        pass

def mock_convert(grammar, node):
    return MockNode() if node == 'node' else node

@pytest.fixture
def parser():
    grammar = MockGrammar()
    parser = Parser(grammar, convert=mock_convert)
    parser.stack = []
    parser.used_names = set()
    return parser

def test_pop_with_non_empty_stack(parser):
    parser.stack.append((None, None, [None, MockNode()]))
    parser.stack.append((None, None, 'node'))
    parser.pop()
    assert isinstance(parser.stack[0][2][-1], MockNode)

def test_pop_with_empty_stack(parser):
    parser.stack.append((None, None, 'node'))
    parser.pop()
    assert isinstance(parser.rootnode, MockNode)
    assert parser.rootnode.used_names == parser.used_names
