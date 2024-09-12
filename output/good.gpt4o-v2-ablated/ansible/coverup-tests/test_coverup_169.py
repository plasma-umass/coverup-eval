# file: lib/ansible/module_utils/facts/system/cmdline.py:68-79
# asked: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}
# gained: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
from unittest.mock import patch

class TestCmdLineFactCollector:
    
    @patch.object(CmdLineFactCollector, '_get_proc_cmdline')
    @patch.object(CmdLineFactCollector, '_parse_proc_cmdline')
    @patch.object(CmdLineFactCollector, '_parse_proc_cmdline_facts')
    def test_collect_with_data(self, mock_parse_proc_cmdline_facts, mock_parse_proc_cmdline, mock_get_proc_cmdline):
        mock_get_proc_cmdline.return_value = 'mocked data'
        mock_parse_proc_cmdline.return_value = 'parsed cmdline'
        mock_parse_proc_cmdline_facts.return_value = 'parsed proc_cmdline'
        
        collector = CmdLineFactCollector()
        result = collector.collect()
        
        assert result == {
            'cmdline': 'parsed cmdline',
            'proc_cmdline': 'parsed proc_cmdline'
        }
        mock_get_proc_cmdline.assert_called_once()
        mock_parse_proc_cmdline.assert_called_once_with('mocked data')
        mock_parse_proc_cmdline_facts.assert_called_once_with('mocked data')
    
    @patch.object(CmdLineFactCollector, '_get_proc_cmdline')
    def test_collect_without_data(self, mock_get_proc_cmdline):
        mock_get_proc_cmdline.return_value = ''
        
        collector = CmdLineFactCollector()
        result = collector.collect()
        
        assert result == {}
        mock_get_proc_cmdline.assert_called_once()
