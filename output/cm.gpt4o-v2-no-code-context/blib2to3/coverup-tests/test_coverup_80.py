# file: src/blib2to3/pytree.py:917-948
# asked: {"lines": [], "branches": [[942, 0]]}
# gained: {"lines": [], "branches": [[942, 0]]}

import pytest
from blib2to3.pytree import BasePattern, NegatedPattern

class MockPattern(BasePattern):
    def generate_matches(self, nodes):
        if not nodes:
            yield 0, {}
        else:
            return

def test_negated_pattern_generate_matches_empty_sequence():
    pattern = NegatedPattern()
    nodes = []
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_non_empty_sequence():
    pattern = NegatedPattern()
    nodes = [1, 2, 3]
    matches = list(pattern.generate_matches(nodes))
    assert matches == []

def test_negated_pattern_with_content_no_match():
    content_pattern = MockPattern()
    pattern = NegatedPattern(content=content_pattern)
    nodes = [1, 2, 3]
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(0, {})]

def test_negated_pattern_with_content_match():
    content_pattern = MockPattern()
    pattern = NegatedPattern(content=content_pattern)
    nodes = []
    matches = list(pattern.generate_matches(nodes))
    assert matches == []

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    yield
    monkeypatch.undo()
