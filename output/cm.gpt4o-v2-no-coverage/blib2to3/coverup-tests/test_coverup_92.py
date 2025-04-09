# file: src/blib2to3/pytree.py:679-704
# asked: {"lines": [700], "branches": [[695, 697], [699, 700]]}
# gained: {"lines": [700], "branches": [[699, 700]]}

import pytest
from unittest.mock import Mock
from blib2to3.pytree import NodePattern, BasePattern, generate_matches

class TestNodePattern:
    @pytest.fixture
    def mock_node(self):
        class MockNode:
            def __init__(self, children):
                self.children = children
        return MockNode

    @pytest.fixture
    def mock_pattern(self):
        class MockPattern(BasePattern):
            def match(self, node, results=None):
                return True
        return MockPattern

    def test_submatch_no_wildcards(self, mock_node, mock_pattern):
        node = mock_node([mock_pattern(), mock_pattern()])
        pattern = NodePattern(type=256, content=[mock_pattern(), mock_pattern()])
        assert pattern._submatch(node) is True

    def test_submatch_with_wildcards(self, mock_node, mock_pattern, monkeypatch):
        node = mock_node([mock_pattern(), mock_pattern()])
        pattern = NodePattern(type=256, content=[mock_pattern(), mock_pattern()])
        pattern.wildcards = True

        def mock_generate_matches(content, children):
            yield (2, {'key': 'value'})

        monkeypatch.setattr('blib2to3.pytree.generate_matches', mock_generate_matches)
        results = {}
        assert pattern._submatch(node, results) is True
        assert results == {'key': 'value'}

    def test_submatch_no_match_length_mismatch(self, mock_node, mock_pattern):
        node = mock_node([mock_pattern()])
        pattern = NodePattern(type=256, content=[mock_pattern(), mock_pattern()])
        assert pattern._submatch(node) is False

    def test_submatch_no_match_content_mismatch(self, mock_node):
        class FailingPattern(BasePattern):
            def match(self, node, results=None):
                return False

        node = mock_node([FailingPattern(), FailingPattern()])
        pattern = NodePattern(type=256, content=[FailingPattern(), FailingPattern()])
        assert pattern._submatch(node) is False
