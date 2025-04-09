# file lib/ansible/module_utils/facts/system/cmdline.py:68-79
# lines [68, 69, 71, 73, 74, 76, 77, 79]
# branches ['73->74', '73->76']

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def mock_get_proc_cmdline(mocker):
    return mocker.patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._get_proc_cmdline')

@pytest.fixture
def mock_parse_proc_cmdline(mocker):
    return mocker.patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._parse_proc_cmdline')

@pytest.fixture
def mock_parse_proc_cmdline_facts(mocker):
    return mocker.patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._parse_proc_cmdline_facts')

def test_collect_no_data(mock_get_proc_cmdline):
    mock_get_proc_cmdline.return_value = None
    collector = CmdLineFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_with_data(mock_get_proc_cmdline, mock_parse_proc_cmdline, mock_parse_proc_cmdline_facts):
    mock_get_proc_cmdline.return_value = "mocked data"
    mock_parse_proc_cmdline.return_value = "parsed cmdline"
    mock_parse_proc_cmdline_facts.return_value = "parsed proc_cmdline"
    
    collector = CmdLineFactCollector()
    result = collector.collect()
    
    assert result == {
        'cmdline': "parsed cmdline",
        'proc_cmdline': "parsed proc_cmdline"
    }
    mock_get_proc_cmdline.assert_called_once()
    mock_parse_proc_cmdline.assert_called_once_with("mocked data")
    mock_parse_proc_cmdline_facts.assert_called_once_with("mocked data")
