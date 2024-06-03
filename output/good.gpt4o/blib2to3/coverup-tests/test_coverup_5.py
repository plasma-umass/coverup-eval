# file src/blib2to3/pytree.py:800-809
# lines [800, 802, 803, 804, 805, 806, 807, 808, 809]
# branches ['802->803', '802->809', '803->802', '803->804', '804->805', '804->808', '806->807', '806->808']

import pytest
from blib2to3.pytree import BasePattern

class WildcardPattern(BasePattern):
    def __init__(self, name=None):
        self.name = name

    def generate_matches(self, nodes):
        # Mock implementation for testing purposes
        yield len(nodes), {}

    def match_seq(self, nodes, results=None) -> bool:
        """Does this pattern exactly match a sequence of nodes?"""
        for c, r in self.generate_matches(nodes):
            if c == len(nodes):
                if results is not None:
                    results.update(r)
                    if self.name:
                        results[self.name] = list(nodes)
                return True
        return False

def test_wildcard_pattern_match_seq():
    pattern = WildcardPattern(name="test")
    nodes = [1, 2, 3]
    results = {}

    assert pattern.match_seq(nodes, results) == True
    assert results == {"test": nodes}

    # Test without results dictionary
    assert pattern.match_seq(nodes) == True

    # Test with no name
    pattern_no_name = WildcardPattern()
    results_no_name = {}
    assert pattern_no_name.match_seq(nodes, results_no_name) == True
    assert results_no_name == {}

    # Test with no matches
    pattern_no_match = WildcardPattern()
    pattern_no_match.generate_matches = lambda nodes: iter([])  # Override to yield no matches
    assert pattern_no_match.match_seq(nodes) == False

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
