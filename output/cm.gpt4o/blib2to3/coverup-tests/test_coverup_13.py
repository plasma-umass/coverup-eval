# file src/blib2to3/pytree.py:885-900
# lines [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900]
# branches ['891->892', '891->898', '893->891', '893->894', '894->893', '894->895']

import pytest
from blib2to3.pytree import WildcardPattern, BasePattern

class MockLeaf:
    def __init__(self, match_result):
        self.match_result = match_result

    def match(self, node, results):
        return self.match_result

@pytest.fixture
def mock_nodes():
    class MockNode:
        pass

    return [MockNode() for _ in range(5)]

def test_wildcard_pattern_bare_name_matches(mock_nodes):
    # Create a WildcardPattern instance with mock content
    pattern = WildcardPattern(content=[(MockLeaf(True),)])
    pattern.name = 'test_name'

    # Call the _bare_name_matches method
    count, results = pattern._bare_name_matches(mock_nodes)

    # Assertions to verify postconditions
    assert count == len(mock_nodes)
    assert 'test_name' in results
    assert results['test_name'] == mock_nodes[:count]
