# file: src/blib2to3/pytree.py:679-704
# asked: {"lines": [679, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704], "branches": [[692, 693], [692, 699], [693, 694], [693, 698], [694, 693], [694, 695], [695, 696], [695, 697], [699, 700], [699, 701], [701, 702], [701, 704], [702, 701], [702, 703]]}
# gained: {"lines": [679, 692, 693, 694, 695, 696, 697, 698, 699, 701, 702, 703, 704], "branches": [[692, 693], [692, 699], [693, 694], [693, 698], [694, 693], [694, 695], [695, 696], [699, 701], [701, 702], [701, 704], [702, 701], [702, 703]]}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import NodePattern, BasePattern, WildcardPattern

class TestNodePattern:
    @pytest.fixture
    def mock_node(self):
        return Mock()

    @pytest.fixture
    def mock_results(self):
        return {}

    def test_submatch_no_wildcards_no_content(self, mock_node, mock_results):
        pattern = NodePattern(type=256, content=[])
        mock_node.children = []
        assert pattern._submatch(mock_node, mock_results) is True

    def test_submatch_no_wildcards_with_content(self, mock_node, mock_results):
        subpattern = Mock(spec=BasePattern)
        subpattern.match.return_value = True
        pattern = NodePattern(type=256, content=[subpattern])
        mock_node.children = [Mock()]
        assert pattern._submatch(mock_node, mock_results) is True
        subpattern.match.assert_called_once_with(mock_node.children[0], mock_results)

    def test_submatch_no_wildcards_with_content_mismatch(self, mock_node, mock_results):
        subpattern = Mock(spec=BasePattern)
        subpattern.match.return_value = False
        pattern = NodePattern(type=256, content=[subpattern])
        mock_node.children = [Mock()]
        assert pattern._submatch(mock_node, mock_results) is False
        subpattern.match.assert_called_once_with(mock_node.children[0], mock_results)

    def test_submatch_with_wildcards(self, mock_node, mock_results, monkeypatch):
        subpattern = Mock(spec=WildcardPattern)
        pattern = NodePattern(type=256, content=[subpattern])
        pattern.wildcards = True
        mock_node.children = [Mock()]

        def mock_generate_matches(content, children):
            yield (1, {'key': 'value'})

        monkeypatch.setattr('blib2to3.pytree.generate_matches', mock_generate_matches)
        assert pattern._submatch(mock_node, mock_results) is True
        assert mock_results == {'key': 'value'}

    def test_submatch_with_wildcards_no_match(self, mock_node, mock_results, monkeypatch):
        subpattern = Mock(spec=WildcardPattern)
        pattern = NodePattern(type=256, content=[subpattern])
        pattern.wildcards = True
        mock_node.children = [Mock()]

        def mock_generate_matches(content, children):
            yield (0, {})

        monkeypatch.setattr('blib2to3.pytree.generate_matches', mock_generate_matches)
        assert pattern._submatch(mock_node, mock_results) is False
