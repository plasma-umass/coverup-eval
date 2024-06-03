# file src/blib2to3/pytree.py:917-948
# lines [927, 928, 929, 933, 937, 940, 942, 943, 946, 947, 948]
# branches ['927->928', '927->929', '940->942', '940->946', '942->exit', '942->943', '946->947', '946->948']

import pytest
from blib2to3.pytree import BasePattern, NegatedPattern

class DummyPattern(BasePattern):
    def match(self, node, results=None) -> bool:
        return True

    def match_seq(self, nodes, results=None) -> bool:
        return len(nodes) == 1

    def generate_matches(self, nodes):
        if len(nodes) == 1:
            yield 0, {}

def test_negated_pattern_with_content():
    content = DummyPattern()
    pattern = NegatedPattern(content)
    
    # Test __init__ with content
    assert pattern.content is content

    # Test match method
    assert not pattern.match(None)

    # Test match_seq method
    assert not pattern.match_seq([1])
    assert pattern.match_seq([])

    # Test generate_matches method with non-empty nodes
    matches = list(pattern.generate_matches([1]))
    assert matches == []

    # Test generate_matches method with empty nodes
    matches = list(pattern.generate_matches([]))
    assert matches == [(0, {})]

def test_negated_pattern_without_content():
    pattern = NegatedPattern()

    # Test __init__ without content
    assert pattern.content is None

    # Test match method
    assert not pattern.match(None)

    # Test match_seq method
    assert not pattern.match_seq([1])
    assert pattern.match_seq([])

    # Test generate_matches method with empty nodes
    matches = list(pattern.generate_matches([]))
    assert matches == [(0, {})]

    # Test generate_matches method with non-empty nodes
    matches = list(pattern.generate_matches([1]))
    assert matches == []

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
