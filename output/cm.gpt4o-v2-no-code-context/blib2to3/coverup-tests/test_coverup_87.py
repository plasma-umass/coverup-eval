# file: src/blib2to3/pytree.py:811-854
# asked: {"lines": [], "branches": [[827, 829], [837, 840], [842, 844], [849, 851], [853, 0]]}
# gained: {"lines": [], "branches": [[842, 844]]}

import pytest
from io import StringIO
import sys
from blib2to3.pytree import BasePattern, WildcardPattern

class MockNode:
    pass

@pytest.fixture
def wildcard_pattern():
    class TestWildcardPattern(WildcardPattern):
        def __init__(self, content=None, name=None, min=0, max=sys.maxsize):
            self.content = content
            self.name = name
            self.min = min
            self.max = max

        def _recursive_matches(self, nodes, start):
            yield (1, {})

        def _iterative_matches(self, nodes):
            yield (1, {})

        def _bare_name_matches(self, nodes):
            return (1, {})

    return TestWildcardPattern

def test_generate_matches_no_content(wildcard_pattern):
    pattern = wildcard_pattern(content=None, name="test_name", min=1, max=2)
    nodes = [MockNode(), MockNode()]
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {"test_name": nodes[:1]}), (2, {"test_name": nodes[:2]})]

def test_generate_matches_bare_name(wildcard_pattern):
    pattern = wildcard_pattern(content="some_content", name="bare_name")
    nodes = [MockNode()]
    matches = list(pattern.generate_matches(nodes))
    assert matches == [(1, {})]

def test_generate_matches_recursive(wildcard_pattern, monkeypatch):
    pattern = wildcard_pattern(content="some_content", name="test_name")
    nodes = [MockNode()]

    def mock_getrefcount(obj):
        return 1

    monkeypatch.setattr(sys, "getrefcount", mock_getrefcount)
    save_stderr = sys.stderr
    sys.stderr = StringIO()

    try:
        matches = list(pattern.generate_matches(nodes))
        assert matches == [(1, {"test_name": nodes[:1]})]
    finally:
        sys.stderr = save_stderr

def test_generate_matches_recursive_runtime_error(wildcard_pattern, monkeypatch):
    pattern = wildcard_pattern(content="some_content", name="test_name")
    nodes = [MockNode()]

    def mock_getrefcount(obj):
        return 1

    def mock_recursive_matches(nodes, start):
        raise RuntimeError

    monkeypatch.setattr(sys, "getrefcount", mock_getrefcount)
    monkeypatch.setattr(pattern, "_recursive_matches", mock_recursive_matches)
    save_stderr = sys.stderr
    sys.stderr = StringIO()

    try:
        matches = list(pattern.generate_matches(nodes))
        assert matches == [(1, {"test_name": nodes[:1]})]
    finally:
        sys.stderr = save_stderr

def test_generate_matches_no_name(wildcard_pattern, monkeypatch):
    pattern = wildcard_pattern(content="some_content", name=None)
    nodes = [MockNode()]

    def mock_getrefcount(obj):
        return 1

    monkeypatch.setattr(sys, "getrefcount", mock_getrefcount)
    save_stderr = sys.stderr
    sys.stderr = StringIO()

    try:
        matches = list(pattern.generate_matches(nodes))
        assert matches == [(1, {})]
    finally:
        sys.stderr = save_stderr

def test_generate_matches_iterative(wildcard_pattern, monkeypatch):
    pattern = wildcard_pattern(content="some_content", name="test_name")
    nodes = [MockNode()]

    def mock_getrefcount(obj):
        return 1

    def mock_recursive_matches(nodes, start):
        raise RuntimeError

    monkeypatch.setattr(sys, "getrefcount", mock_getrefcount)
    monkeypatch.setattr(pattern, "_recursive_matches", mock_recursive_matches)
    save_stderr = sys.stderr
    sys.stderr = StringIO()

    try:
        matches = list(pattern.generate_matches(nodes))
        assert matches == [(1, {"test_name": nodes[:1]})]
    finally:
        sys.stderr = save_stderr
