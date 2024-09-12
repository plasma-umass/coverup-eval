# file: src/blib2to3/pytree.py:811-854
# asked: {"lines": [823, 825, 826, 827, 828, 829, 830, 831, 837, 838, 839, 840, 841, 842, 843, 844, 845, 848, 849, 850, 851, 853, 854], "branches": [[823, 825], [823, 830], [825, 0], [825, 826], [827, 828], [827, 829], [830, 831], [830, 837], [837, 838], [837, 840], [841, 842], [841, 853], [842, 843], [842, 844], [848, 849], [848, 853], [849, 850], [849, 851], [853, 0], [853, 854]]}
# gained: {"lines": [823, 825, 826, 827, 828, 829, 830, 831, 837, 838, 839, 840, 841, 842, 843, 844, 845, 848, 849, 850, 851, 853, 854], "branches": [[823, 825], [823, 830], [825, 0], [825, 826], [827, 828], [830, 831], [830, 837], [837, 838], [841, 842], [841, 853], [842, 843], [848, 849], [848, 853], [849, 850], [853, 854]]}

import pytest
from blib2to3.pytree import WildcardPattern
from io import StringIO
import sys

@pytest.fixture
def setup_wildcard_pattern():
    # Setup a WildcardPattern instance
    content = [[MockLeaf('a'), MockLeaf('b')], [MockLeaf('c')]]
    pattern = WildcardPattern(content=content, min=1, max=2, name="test")
    return pattern

class MockLeaf:
    def __init__(self, value):
        self.value = value

    def match(self, node, results):
        return self.value == node

def test_generate_matches_shortcut(setup_wildcard_pattern):
    pattern = setup_wildcard_pattern
    pattern.content = None  # Trigger the shortcut case
    nodes = ['a', 'b', 'c']
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {'test': ['a']}), (2, {'test': ['a', 'b']})]

def test_generate_matches_bare_name(monkeypatch, setup_wildcard_pattern):
    pattern = setup_wildcard_pattern
    pattern.name = "bare_name"  # Trigger the bare_name case

    def mock_bare_name_matches(nodes):
        return (1, {'bare_name': nodes[:1]})

    monkeypatch.setattr(pattern, "_bare_name_matches", mock_bare_name_matches)
    nodes = ['a', 'b', 'c']
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {'bare_name': ['a']})]

def test_generate_matches_recursive(monkeypatch, setup_wildcard_pattern):
    pattern = setup_wildcard_pattern

    def mock_recursive_matches(nodes, count):
        yield (1, {'recursive': nodes[:1]})

    monkeypatch.setattr(pattern, "_recursive_matches", mock_recursive_matches)
    nodes = ['a', 'b', 'c']
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {'test': ['a'], 'recursive': ['a']})]

def test_generate_matches_iterative(monkeypatch, setup_wildcard_pattern):
    pattern = setup_wildcard_pattern

    def mock_recursive_matches(nodes, count):
        raise RuntimeError

    def mock_iterative_matches(nodes):
        yield (1, {'iterative': nodes[:1]})

    monkeypatch.setattr(pattern, "_recursive_matches", mock_recursive_matches)
    monkeypatch.setattr(pattern, "_iterative_matches", mock_iterative_matches)
    nodes = ['a', 'b', 'c']
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {'test': ['a'], 'iterative': ['a']})]

def test_generate_matches_sys_stderr(monkeypatch, setup_wildcard_pattern):
    pattern = setup_wildcard_pattern

    def mock_recursive_matches(nodes, count):
        yield (1, {'recursive': nodes[:1]})

    monkeypatch.setattr(pattern, "_recursive_matches", mock_recursive_matches)
    monkeypatch.setattr(sys, "getrefcount", lambda x: 1)
    save_stderr = sys.stderr
    sys.stderr = StringIO()
    try:
        nodes = ['a', 'b', 'c']
        matches = list(pattern.generate_matches(nodes))
        assert matches == [(1, {'test': ['a'], 'recursive': ['a']})]
    finally:
        sys.stderr = save_stderr
