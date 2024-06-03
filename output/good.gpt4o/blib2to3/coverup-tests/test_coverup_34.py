# file src/blib2to3/pytree.py:679-704
# lines [679, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704]
# branches ['692->693', '692->699', '693->694', '693->698', '694->693', '694->695', '695->696', '695->697', '699->700', '699->701', '701->702', '701->704', '702->701', '702->703']

import pytest
from blib2to3.pytree import NodePattern, BasePattern, Node
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2.token import tok_name

class MockPattern(BasePattern):
    def __init__(self, match_result):
        self.match_result = match_result

    def match(self, node, results=None):
        return self.match_result

def generate_matches(content, children):
    # Mock implementation of generate_matches
    yield len(children), {}

@pytest.fixture
def mock_generate_matches(mocker):
    return mocker.patch('blib2to3.pytree.generate_matches', side_effect=generate_matches)

@pytest.fixture
def grammar():
    g = Grammar()
    g.symbol2number['file_input'] = 256
    return g

def test_node_pattern_submatch_wildcards(mock_generate_matches, grammar):
    pattern = NodePattern(type=256, content=[MockPattern(True)])
    pattern.wildcards = True
    node = Node(grammar.symbol2number['file_input'], [])
    results = {}

    assert pattern._submatch(node, results) is True
    assert results == {}

def test_node_pattern_submatch_no_wildcards_length_mismatch(grammar):
    pattern = NodePattern(type=256, content=[MockPattern(True)])
    pattern.wildcards = False
    node = Node(grammar.symbol2number['file_input'], [])
    results = {}

    assert pattern._submatch(node, results) is False

def test_node_pattern_submatch_no_wildcards_match_failure(grammar):
    pattern = NodePattern(type=256, content=[MockPattern(False)])
    pattern.wildcards = False
    node = Node(grammar.symbol2number['file_input'], [Node(grammar.symbol2number['file_input'], [])])
    results = {}

    assert pattern._submatch(node, results) is False

def test_node_pattern_submatch_no_wildcards_match_success(grammar):
    pattern = NodePattern(type=256, content=[MockPattern(True)])
    pattern.wildcards = False
    node = Node(grammar.symbol2number['file_input'], [Node(grammar.symbol2number['file_input'], [])])
    results = {}

    assert pattern._submatch(node, results) is True
