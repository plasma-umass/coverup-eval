# file: src/blib2to3/pytree.py:679-704
# asked: {"lines": [679, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704], "branches": [[692, 693], [692, 699], [693, 694], [693, 698], [694, 693], [694, 695], [695, 696], [695, 697], [699, 700], [699, 701], [701, 702], [701, 704], [702, 701], [702, 703]]}
# gained: {"lines": [679, 692, 693, 694, 695, 697, 698, 699, 700, 701, 702, 703, 704], "branches": [[692, 693], [692, 699], [693, 694], [693, 698], [694, 695], [695, 697], [699, 700], [699, 701], [701, 702], [701, 704], [702, 701], [702, 703]]}

import pytest
from blib2to3.pytree import NodePattern, BasePattern, generate_matches
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2.driver import Driver
from blib2to3.pgen2.parse import ParseError
from blib2to3.pytree import Node, Leaf

class MockPattern(BasePattern):
    def __init__(self, match_result):
        self.match_result = match_result

    def match(self, node, results=None):
        return self.match_result

class MockWildcardPattern(MockPattern):
    pass

@pytest.fixture
def mock_node():
    return Node(256, [Leaf(1, "a"), Leaf(1, "b")])

def test_submatch_no_wildcards(mock_node):
    pattern = NodePattern(type=256, content=[MockPattern(True), MockPattern(True)])
    assert pattern._submatch(mock_node) is True

def test_submatch_with_wildcards(mock_node, mocker):
    pattern = NodePattern(type=256, content=[MockWildcardPattern(True), MockWildcardPattern(True)])
    pattern.wildcards = True
    mocker.patch('blib2to3.pytree.generate_matches', return_value=iter([(2, {})]))
    assert pattern._submatch(mock_node) is True

def test_submatch_with_wildcards_no_match(mock_node, mocker):
    pattern = NodePattern(type=256, content=[MockWildcardPattern(True), MockWildcardPattern(True)])
    pattern.wildcards = True
    mocker.patch('blib2to3.pytree.generate_matches', return_value=iter([]))
    assert pattern._submatch(mock_node) is False

def test_submatch_length_mismatch(mock_node):
    pattern = NodePattern(type=256, content=[MockPattern(True)])
    assert pattern._submatch(mock_node) is False

def test_submatch_child_mismatch(mock_node):
    pattern = NodePattern(type=256, content=[MockPattern(False), MockPattern(True)])
    assert pattern._submatch(mock_node) is False
