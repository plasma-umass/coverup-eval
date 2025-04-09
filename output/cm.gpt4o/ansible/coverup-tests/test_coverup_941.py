# file lib/ansible/module_utils/facts/system/cmdline.py:30-31
# lines [30, 31]
# branches []

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.cmdline.get_file_content')

def test_get_proc_cmdline(mock_get_file_content):
    mock_get_file_content.return_value = 'mocked cmdline content'
    
    collector = CmdLineFactCollector()
    result = collector._get_proc_cmdline()
    
    assert result == 'mocked cmdline content'
    mock_get_file_content.assert_called_once_with('/proc/cmdline')
