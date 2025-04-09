# file: src/blib2to3/pytree.py:917-948
# asked: {"lines": [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 0], [942, 943], [946, 947], [946, 948]]}
# gained: {"lines": [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 0], [942, 943], [946, 947], [946, 948]]}

import pytest
from blib2to3.pytree import NegatedPattern, BasePattern

class MockPattern(BasePattern):
    def generate_matches(self, nodes):
        if nodes == [1, 2, 3]:
            yield (1, {})
        else:
            return

def test_negated_pattern_init_with_content():
    content = MockPattern()
    pattern = NegatedPattern(content)
    assert pattern.content is content

def test_negated_pattern_init_without_content():
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

def test_negated_pattern_generate_matches_with_none_content():
    pattern = NegatedPattern()
    matches = list(pattern.generate_matches([]))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_with_none_content_non_empty_nodes():
    pattern = NegatedPattern()
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == []

def test_negated_pattern_generate_matches_with_content_no_match():
    content = MockPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([4, 5, 6]))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_with_content_with_match():
    content = MockPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == []

