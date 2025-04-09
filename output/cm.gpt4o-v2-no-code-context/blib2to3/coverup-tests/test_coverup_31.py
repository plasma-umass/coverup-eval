# file: src/blib2to3/pytree.py:572-580
# asked: {"lines": [572, 578, 579, 580], "branches": [[578, 579], [578, 580]]}
# gained: {"lines": [572, 578, 579, 580], "branches": [[578, 579], [578, 580]]}

import pytest
from blib2to3.pytree import BasePattern

class MockNode:
    pass

class MockPattern(BasePattern):
    def match(self, node, results):
        return True

def test_match_seq_single_node():
    pattern = MockPattern()
    nodes = [MockNode()]
    results = {}
    assert pattern.match_seq(nodes, results) == True

def test_match_seq_multiple_nodes():
    pattern = MockPattern()
    nodes = [MockNode(), MockNode()]
    results = {}
    assert pattern.match_seq(nodes, results) == False
