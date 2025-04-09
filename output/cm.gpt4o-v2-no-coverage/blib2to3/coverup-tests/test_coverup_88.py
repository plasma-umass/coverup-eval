# file: src/blib2to3/pytree.py:885-900
# asked: {"lines": [887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 891], [893, 894], [894, 893], [894, 895]]}
# gained: {"lines": [887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 891], [893, 894], [894, 893], [894, 895]]}

import pytest
from blib2to3.pytree import WildcardPattern, BasePattern

class MockNode:
    def __init__(self, value):
        self.value = value

    def match(self, node, results):
        return self.value == node.value

def test_bare_name_matches():
    # Setup
    nodes = [MockNode(1), MockNode(2), MockNode(3)]
    pattern_content = [(MockNode(1),), (MockNode(2),)]
    pattern = WildcardPattern(content=pattern_content, name="test")

    # Execute
    count, results = pattern._bare_name_matches(nodes)

    # Verify
    assert count == 2
    assert results == {"test": nodes[:2]}

    # Cleanup
    del pattern
    del nodes
    del pattern_content
    del count
    del results

@pytest.fixture
def mock_nodes():
    return [MockNode(1), MockNode(2), MockNode(3)]

def test_bare_name_matches_with_fixture(mock_nodes):
    # Setup
    pattern_content = [(MockNode(1),), (MockNode(2),)]
    pattern = WildcardPattern(content=pattern_content, name="test")

    # Execute
    count, results = pattern._bare_name_matches(mock_nodes)

    # Verify
    assert count == 2
    assert results == {"test": mock_nodes[:2]}

    # Cleanup
    del pattern
    del pattern_content
    del count
    del results
