# file: src/blib2to3/pytree.py:885-900
# asked: {"lines": [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 891], [893, 894], [894, 893], [894, 895]]}
# gained: {"lines": [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 894], [894, 895]]}

import pytest
from blib2to3.pytree import WildcardPattern, BasePattern

class MockNode:
    def __init__(self, value):
        self.value = value

    def match(self, node, results):
        results[self.value] = node
        return True

def test_bare_name_matches():
    # Create a mock content for WildcardPattern
    content = [(MockNode('a'),), (MockNode('b'),)]
    pattern = WildcardPattern(content=content, name='test')

    # Create a list of nodes to match
    nodes = [MockNode('a'), MockNode('b')]

    # Call the _bare_name_matches method
    count, results = pattern._bare_name_matches(nodes)

    # Assertions to verify the postconditions
    assert count == 2
    assert 'test' in results
    assert results['test'] == nodes

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Monkeypatch or mock any global state if necessary
    yield
    # Teardown: Clean up any state to avoid pollution
