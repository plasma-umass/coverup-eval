# file src/blib2to3/pytree.py:917-948
# lines [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948]
# branches ['927->928', '927->929', '940->942', '940->946', '942->exit', '942->943', '946->947', '946->948']

import pytest
from blib2to3.pytree import BasePattern
from typing import Optional, Any, Iterator, Tuple, Dict

class NegatedPattern(BasePattern):
    def __init__(self, content: Optional[Any] = None) -> None:
        """
        Initializer.

        The argument is either a pattern or None.  If it is None, this
        only matches an empty sequence (effectively '$' in regex
        lingo).  If it is not None, this matches whenever the argument
        pattern doesn't have any matches.
        """
        if content is not None:
            assert isinstance(content, BasePattern), repr(content)
        self.content = content

    def match(self, node, results=None) -> bool:
        # We never match a node in its entirety
        return False

    def match_seq(self, nodes, results=None) -> bool:
        # We only match an empty sequence of nodes in its entirety
        return len(nodes) == 0

    def generate_matches(self, nodes) -> Iterator[Tuple[int, Dict]]:
        if self.content is None:
            # Return a match if there is an empty sequence
            if len(nodes) == 0:
                yield 0, {}
        else:
            # Return a match if the argument pattern has no matches
            for c, r in self.content.generate_matches(nodes):
                return
            yield 0, {}

class MockPattern(BasePattern):
    def generate_matches(self, nodes) -> Iterator[Tuple[int, Dict]]:
        if len(nodes) > 0:
            yield 1, {}
        else:
            return

@pytest.fixture
def mock_pattern():
    return MockPattern()

def test_negated_pattern_with_content(mock_pattern):
    negated_pattern = NegatedPattern(content=mock_pattern)
    nodes = [1, 2, 3]
    matches = list(negated_pattern.generate_matches(nodes))
    assert matches == []

def test_negated_pattern_without_content():
    negated_pattern = NegatedPattern()
    nodes = []
    matches = list(negated_pattern.generate_matches(nodes))
    assert matches == [(0, {})]

def test_negated_pattern_match_seq_with_nodes():
    negated_pattern = NegatedPattern()
    nodes = [1, 2, 3]
    assert not negated_pattern.match_seq(nodes)

def test_negated_pattern_match_seq_without_nodes():
    negated_pattern = NegatedPattern()
    nodes = []
    assert negated_pattern.match_seq(nodes)

def test_negated_pattern_match():
    negated_pattern = NegatedPattern()
    assert not negated_pattern.match(None)
