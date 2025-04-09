# file: lib/ansible/module_utils/facts/other/facter.py:64-85
# asked: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}
# gained: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}

import json
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts.other.facter import FacterFactCollector

class TestFacterFactCollector:
    
    @patch.object(FacterFactCollector, 'get_facter_output')
    def test_collect_no_module(self, mock_get_facter_output):
        collector = FacterFactCollector()
        result = collector.collect(module=None)
        assert result == {}
        mock_get_facter_output.assert_not_called()

    @patch.object(FacterFactCollector, 'get_facter_output')
    def test_collect_facter_output_none(self, mock_get_facter_output):
        collector = FacterFactCollector()
        mock_module = Mock()
        mock_get_facter_output.return_value = None
        result = collector.collect(module=mock_module)
        assert result == {}
        mock_get_facter_output.assert_called_once_with(mock_module)

    @patch.object(FacterFactCollector, 'get_facter_output')
    def test_collect_facter_output_invalid_json(self, mock_get_facter_output):
        collector = FacterFactCollector()
        mock_module = Mock()
        mock_get_facter_output.return_value = "invalid json"
        result = collector.collect(module=mock_module)
        assert result == {}
        mock_get_facter_output.assert_called_once_with(mock_module)

    @patch.object(FacterFactCollector, 'get_facter_output')
    def test_collect_facter_output_valid_json(self, mock_get_facter_output):
        collector = FacterFactCollector()
        mock_module = Mock()
        mock_facter_output = '{"key": "value"}'
        mock_get_facter_output.return_value = mock_facter_output
        result = collector.collect(module=mock_module)
        assert result == {"key": "value"}
        mock_get_facter_output.assert_called_once_with(mock_module)
