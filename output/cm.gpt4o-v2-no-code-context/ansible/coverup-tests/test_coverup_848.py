# file: lib/ansible/module_utils/facts/system/cmdline.py:30-31
# asked: {"lines": [30, 31], "branches": []}
# gained: {"lines": [30, 31], "branches": []}

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

class TestCmdLineFactCollector:
    
    @patch('ansible.module_utils.facts.system.cmdline.get_file_content')
    def test_get_proc_cmdline(self, mock_get_file_content):
        # Arrange
        expected_content = "mocked content"
        mock_get_file_content.return_value = expected_content
        collector = CmdLineFactCollector()
        
        # Act
        result = collector._get_proc_cmdline()
        
        # Assert
        mock_get_file_content.assert_called_once_with('/proc/cmdline')
        assert result == expected_content
