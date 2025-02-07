# file: src/blib2to3/pytree.py:917-948
# asked: {"lines": [927, 928, 929, 933, 937, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 0], [942, 943], [946, 947], [946, 948]]}
# gained: {"lines": [927, 928, 929, 933, 937, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 0], [942, 943], [946, 947], [946, 948]]}

import pytest
from blib2to3.pytree import BasePattern, NegatedPattern

class DummyPattern(BasePattern):
    def generate_matches(self, nodes):
        if not nodes:
            yield 0, {}

def test_negated_pattern_with_content():
    content = DummyPattern()
    pattern = NegatedPattern(content)
    assert pattern.content == content

def test_negated_pattern_without_content():
    pattern = NegatedPattern()
    assert pattern.content is None

def test_negated_pattern_match():
    pattern = NegatedPattern()
    assert not pattern.match(None)

def test_negated_pattern_match_seq_empty():
    pattern = NegatedPattern()
    assert pattern.match_seq([])

def test_negated_pattern_match_seq_non_empty():
    pattern = NegatedPattern()
    assert not pattern.match_seq([1, 2, 3])

def test_negated_pattern_generate_matches_no_content_empty_nodes():
    pattern = NegatedPattern()
    matches = list(pattern.generate_matches([]))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_no_content_non_empty_nodes():
    pattern = NegatedPattern()
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == []

def test_negated_pattern_generate_matches_with_content_no_match():
    content = DummyPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_with_content_match():
    class MatchingPattern(BasePattern):
        def generate_matches(self, nodes):
            if nodes:
                yield 0, {}

    content = MatchingPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == []

