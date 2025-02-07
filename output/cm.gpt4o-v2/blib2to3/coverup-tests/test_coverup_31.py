# file: src/blib2to3/pytree.py:572-580
# asked: {"lines": [572, 578, 579, 580], "branches": [[578, 579], [578, 580]]}
# gained: {"lines": [572, 578, 579, 580], "branches": [[578, 579], [578, 580]]}

import pytest
from blib2to3.pytree import BasePattern

class TestBasePattern(BasePattern):
    def __init__(self, type=None, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

    def _submatch(self, node, results=None):
        return True

def test_match_seq_single_node(mocker):
    pattern = TestBasePattern()
    node = mocker.Mock()
    nodes = [node]
    mocker.patch.object(pattern, 'match', return_value=True)
    
    results = {}
    assert pattern.match_seq(nodes, results) == True
    pattern.match.assert_called_once_with(node, results)

def test_match_seq_multiple_nodes(mocker):
    pattern = TestBasePattern()
    node1 = mocker.Mock()
    node2 = mocker.Mock()
    nodes = [node1, node2]
    
    results = {}
    assert pattern.match_seq(nodes, results) == False
