# file src/blib2to3/pytree.py:917-948
# lines [933, 937]
# branches ['942->exit']

import pytest
from blib2to3.pytree import NegatedPattern, BasePattern

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
    # No cleanup needed for this test
    yield

def test_negated_pattern():
    # Test NegatedPattern with content is None and an empty sequence
    neg_pattern_none = NegatedPattern()
    assert not neg_pattern_none.match(None)
    assert neg_pattern_none.match_seq([])

    # Test NegatedPattern with content is None and a non-empty sequence
    assert not neg_pattern_none.match_seq([1, 2, 3])

    # Test NegatedPattern with content is not None and an empty sequence
    dummy_pattern = DummyPattern()
    neg_pattern_dummy = NegatedPattern(dummy_pattern)
    assert not neg_pattern_dummy.match(None)
    assert neg_pattern_dummy.match_seq([])

    # Test NegatedPattern with content is not None and a non-empty sequence
    assert not neg_pattern_dummy.match_seq([1, 2, 3])

    # Test generate_matches with content is None and an empty sequence
    matches = list(neg_pattern_none.generate_matches([]))
    assert matches == [(0, {})]

    # Test generate_matches with content is None and a non-empty sequence
    matches = list(neg_pattern_none.generate_matches([1, 2, 3]))
    assert matches == []

    # Test generate_matches with content is not None and an empty sequence
    matches = list(neg_pattern_dummy.generate_matches([]))
    assert matches == [(0, {})]

    # Test generate_matches with content is not None and a non-empty sequence
    # The original test expected a match, but since the DummyPattern matches the nodes,
    # the NegatedPattern should not match, hence the expected result should be an empty list.
    matches = list(neg_pattern_dummy.generate_matches([1, 2, 3]))
    assert matches == []
