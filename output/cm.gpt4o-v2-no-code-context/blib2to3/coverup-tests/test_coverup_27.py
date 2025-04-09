# file: src/blib2to3/pytree.py:917-948
# asked: {"lines": [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 0], [942, 943], [946, 947], [946, 948]]}
# gained: {"lines": [917, 918, 927, 928, 929, 931, 933, 935, 937, 939, 940, 942, 943, 946, 947, 948], "branches": [[927, 928], [927, 929], [940, 942], [940, 946], [942, 943], [946, 947], [946, 948]]}

import pytest
from blib2to3.pytree import BasePattern, NegatedPattern

class DummyPattern(BasePattern):
    def generate_matches(self, nodes):
        if not nodes:
            yield 0, {}

def test_negated_pattern_init_with_content():
    content = DummyPattern()
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

def test_negated_pattern_generate_matches_empty_content():
    pattern = NegatedPattern()
    matches = list(pattern.generate_matches([]))
    assert matches == [(0, {})]

def test_negated_pattern_generate_matches_non_empty_content():
    class MatchPattern(BasePattern):
        def generate_matches(self, nodes):
            if nodes:
                yield 0, {}
    content = MatchPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == []

def test_negated_pattern_generate_matches_non_empty_content_no_match():
    class NoMatchPattern(BasePattern):
        def generate_matches(self, nodes):
            if False:
                yield 0, {}
    content = NoMatchPattern()
    pattern = NegatedPattern(content)
    matches = list(pattern.generate_matches([1, 2, 3]))
    assert matches == [(0, {})]
