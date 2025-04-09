# file: src/blib2to3/pytree.py:811-854
# asked: {"lines": [823, 825, 826, 827, 828, 829, 830, 831, 837, 838, 839, 840, 841, 842, 843, 844, 845, 848, 849, 850, 851, 853, 854], "branches": [[823, 825], [823, 830], [825, 0], [825, 826], [827, 828], [827, 829], [830, 831], [830, 837], [837, 838], [837, 840], [841, 842], [841, 853], [842, 843], [842, 844], [848, 849], [848, 853], [849, 850], [849, 851], [853, 0], [853, 854]]}
# gained: {"lines": [823, 825, 826, 827, 828, 829, 830, 831, 837, 838, 839, 840, 841, 842, 843, 844, 845, 848, 849, 850, 851, 853, 854], "branches": [[823, 825], [823, 830], [825, 0], [825, 826], [827, 828], [830, 831], [830, 837], [837, 838], [841, 842], [841, 853], [842, 843], [848, 849], [848, 853], [849, 850], [853, 854]]}

import pytest
from io import StringIO
import sys
from blib2to3.pytree import BasePattern, WildcardPattern

class TestWildcardPattern:
    @pytest.fixture
    def wildcard_pattern(self):
        # Create a valid content to avoid UnboundLocalError
        content = [["a"], ["b"]]
        return WildcardPattern(content=content)

    def test_generate_matches_shortcut(self, wildcard_pattern):
        wildcard_pattern.content = None
        wildcard_pattern.min = 1
        wildcard_pattern.max = 3
        wildcard_pattern.name = "test"
        nodes = [1, 2, 3, 4]

        matches = list(wildcard_pattern.generate_matches(nodes))
        assert matches == [
            (1, {"test": [1]}),
            (2, {"test": [1, 2]}),
            (3, {"test": [1, 2, 3]})
        ]

    def test_generate_matches_bare_name(self, monkeypatch, wildcard_pattern):
        def mock_bare_name_matches(nodes):
            return 1, {"bare_name": nodes[:1]}

        monkeypatch.setattr(wildcard_pattern, "_bare_name_matches", mock_bare_name_matches)
        wildcard_pattern.name = "bare_name"
        nodes = [1, 2, 3]

        matches = list(wildcard_pattern.generate_matches(nodes))
        assert matches == [(1, {"bare_name": [1]})]

    def test_generate_matches_recursive(self, monkeypatch, wildcard_pattern):
        def mock_recursive_matches(nodes, depth):
            yield 2, {"recursive": nodes[:2]}

        monkeypatch.setattr(wildcard_pattern, "_recursive_matches", mock_recursive_matches)
        wildcard_pattern.name = "recursive"
        nodes = [1, 2, 3]

        matches = list(wildcard_pattern.generate_matches(nodes))
        assert matches == [(2, {"recursive": [1, 2], "recursive": [1, 2]})]

    def test_generate_matches_iterative_fallback(self, monkeypatch, wildcard_pattern):
        def mock_recursive_matches(nodes, depth):
            raise RuntimeError

        def mock_iterative_matches(nodes):
            yield 1, {"iterative": nodes[:1]}

        monkeypatch.setattr(wildcard_pattern, "_recursive_matches", mock_recursive_matches)
        monkeypatch.setattr(wildcard_pattern, "_iterative_matches", mock_iterative_matches)
        wildcard_pattern.name = "iterative"
        nodes = [1, 2, 3]

        matches = list(wildcard_pattern.generate_matches(nodes))
        assert matches == [(1, {"iterative": [1], "iterative": [1]})]

    def test_generate_matches_sys_stderr(self, monkeypatch, wildcard_pattern):
        def mock_recursive_matches(nodes, depth):
            yield 2, {"recursive": nodes[:2]}

        monkeypatch.setattr(wildcard_pattern, "_recursive_matches", mock_recursive_matches)
        wildcard_pattern.name = "recursive"
        nodes = [1, 2, 3]

        if hasattr(sys, "getrefcount"):
            save_stderr = sys.stderr
            sys.stderr = StringIO()

        try:
            matches = list(wildcard_pattern.generate_matches(nodes))
            assert matches == [(2, {"recursive": [1, 2], "recursive": [1, 2]})]
        finally:
            if hasattr(sys, "getrefcount"):
                sys.stderr = save_stderr
