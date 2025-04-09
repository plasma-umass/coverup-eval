# file: src/blib2to3/pytree.py:902-914
# asked: {"lines": [902, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914], "branches": [[905, 906], [905, 907], [907, 0], [907, 908], [908, 0], [908, 909], [909, 908], [909, 910], [910, 909], [910, 911]]}
# gained: {"lines": [902, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914], "branches": [[905, 906], [907, 0], [907, 908], [908, 0], [908, 909], [909, 908], [909, 910], [910, 909], [910, 911]]}

import pytest
from blib2to3.pytree import WildcardPattern, generate_matches

class MockPattern:
    def __init__(self, matches):
        self.matches = matches

    def generate_matches(self, nodes):
        for match in self.matches:
            yield match

def test_recursive_matches_min(monkeypatch):
    # Mock content to control the behavior of generate_matches
    mock_content = [[MockPattern([(1, {'a': 1})])]]
    pattern = WildcardPattern(content=mock_content, min=1, max=2)

    nodes = ['node1', 'node2']
    matches = list(pattern._recursive_matches(nodes, 1))

    assert matches == [(0, {}), (1, {'a': 1})]

def test_recursive_matches_max(monkeypatch):
    # Mock content to control the behavior of generate_matches
    mock_content = [[MockPattern([(1, {'a': 1})])]]
    pattern = WildcardPattern(content=mock_content, min=0, max=1)

    nodes = ['node1', 'node2']
    matches = list(pattern._recursive_matches(nodes, 0))

    assert matches == [(0, {}), (1, {'a': 1})]

def test_recursive_matches_update(monkeypatch):
    # Mock content to control the behavior of generate_matches
    mock_content = [[MockPattern([(1, {'a': 1})])]]
    pattern = WildcardPattern(content=mock_content, min=0, max=2)

    nodes = ['node1', 'node2']
    matches = list(pattern._recursive_matches(nodes, 0))

    assert matches == [(0, {}), (1, {'a': 1}), (2, {'a': 1})]
