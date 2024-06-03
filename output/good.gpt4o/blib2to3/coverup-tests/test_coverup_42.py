# file src/blib2to3/pytree.py:572-580
# lines [572, 578, 579, 580]
# branches ['578->579', '578->580']

import pytest
from unittest.mock import Mock
from blib2to3.pytree import BasePattern

class ConcretePattern(BasePattern):
    def match(self, node, results):
        return True

class TestBasePattern:
    def test_match_seq_single_node(self):
        # Arrange
        pattern = ConcretePattern()
        node = Mock()
        results = {}

        # Act
        result = pattern.match_seq([node], results)

        # Assert
        assert result is True

    def test_match_seq_multiple_nodes(self):
        # Arrange
        pattern = ConcretePattern()
        nodes = [Mock(), Mock()]
        results = {}

        # Act
        result = pattern.match_seq(nodes, results)

        # Assert
        assert result is False

    def test_match_seq_no_nodes(self):
        # Arrange
        pattern = ConcretePattern()
        nodes = []
        results = {}

        # Act
        result = pattern.match_seq(nodes, results)

        # Assert
        assert result is False
