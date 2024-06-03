# file src/blib2to3/pgen2/parse.py:226-237
# lines [228, 229, 230, 231, 232, 233, 234, 236, 237]
# branches ['230->exit', '230->231', '231->232', '231->236']

import pytest
from blib2to3.pgen2.parse import Parser

class MockGrammar:
    pass

class MockNode:
    def __init__(self):
        self.children = []

    def append(self, node):
        self.children.append(node)

@pytest.fixture
def parser():
    grammar = MockGrammar()
    parser = Parser(grammar)
    parser.stack = []
    parser.used_names = set()
    return parser

def test_pop_with_stack(parser, mocker):
    mock_node = MockNode()
    parser.stack.append((None, None, [mock_node]))
    parser.stack.append((None, None, [None]))
    
    mock_convert = mocker.patch.object(parser, 'convert', return_value=mock_node)
    
    parser.pop()
    
    assert len(parser.stack) == 1
    assert parser.stack[0][2][0].children == [mock_node]
    mock_convert.assert_called_once_with(parser.grammar, [None])

def test_pop_without_stack(parser, mocker):
    mock_node = MockNode()
    parser.stack.append((None, None, [None]))
    
    mock_convert = mocker.patch.object(parser, 'convert', return_value=mock_node)
    
    parser.pop()
    
    assert len(parser.stack) == 0
    assert parser.rootnode == mock_node
    assert parser.rootnode.used_names == parser.used_names
    mock_convert.assert_called_once_with(parser.grammar, [None])
