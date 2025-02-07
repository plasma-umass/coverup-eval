# file: lib/ansible/module_utils/facts/system/cmdline.py:30-31
# asked: {"lines": [31], "branches": []}
# gained: {"lines": [31], "branches": []}

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_get_proc_cmdline_reads_file(cmdline_collector):
    mock_data = "mock cmdline data"
    with patch("ansible.module_utils.facts.system.cmdline.get_file_content", return_value=mock_data) as mock_get_file_content:
        result = cmdline_collector._get_proc_cmdline()
        mock_get_file_content.assert_called_once_with('/proc/cmdline')
        assert result == mock_data

def test_get_proc_cmdline_file_not_found(cmdline_collector):
    with patch("ansible.module_utils.facts.system.cmdline.get_file_content", return_value=None) as mock_get_file_content:
        result = cmdline_collector._get_proc_cmdline()
        mock_get_file_content.assert_called_once_with('/proc/cmdline')
        assert result is None
