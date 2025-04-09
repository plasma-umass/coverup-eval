# file src/blib2to3/pytree.py:917-948
# lines [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948]
# branches ['927->928', '927->929', '940->942', '940->946', '942->exit', '942->943', '946->947', '946->948']

import pytest
from blib2to3.pytree import BasePattern, NegatedPattern

class DummyPattern(BasePattern):
    def match(self, node, results=None):
        return True

    def match_seq(self, nodes, results=None):
        return True

    def generate_matches(self, nodes):
        if nodes:
            yield 1, {}

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup after tests
    yield
    # No specific cleanup required for this test

def test_negated_pattern_with_content(cleanup):
    pattern = NegatedPattern(content=DummyPattern())
    nodes = ['node1', 'node2']
    matches = list(pattern.generate_matches(nodes))
    assert matches == [], "NegatedPattern with content should not match non-empty node list"

def test_negated_pattern_without_content(cleanup):
    pattern = NegatedPattern()
    nodes = []
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(0, {})], "NegatedPattern without content should match empty node list"

def test_negated_pattern_with_content_empty_nodes(cleanup):
    pattern = NegatedPattern(content=DummyPattern())
    nodes = []
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(0, {})], "NegatedPattern with content should match empty node list"
