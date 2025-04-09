# file lib/ansible/module_utils/facts/system/cmdline.py:33-45
# lines [33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 45]
# branches ['36->37', '36->45', '38->39', '38->41']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
from unittest.mock import mock_open, patch

@pytest.fixture
def cmd_line_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_single_item(cmd_line_collector):
    data = "single_item"
    result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {"single_item": True}

def test_parse_proc_cmdline_key_value(cmd_line_collector):
    data = "key=value"
    result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {"key": "value"}

def test_parse_proc_cmdline_with_quotes(cmd_line_collector):
    data = 'key="value with spaces" another_key=another_value'
    with patch('shlex.split', return_value=['key=value with spaces', 'another_key=another_value']):
        result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {"key": "value with spaces", "another_key": "another_value"}

def test_parse_proc_cmdline_with_incomplete_quotes(cmd_line_collector):
    data = 'key="value with spaces another_key=another_value'
    with patch('shlex.split', side_effect=ValueError):
        result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {}

def test_parse_proc_cmdline_with_malformed_data(cmd_line_collector):
    data = "key=value with spaces another_key=another_value"
    with patch('shlex.split', side_effect=ValueError):
        result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {}

def test_parse_proc_cmdline_with_empty_data(cmd_line_collector):
    data = ""
    result = cmd_line_collector._parse_proc_cmdline(data)
    assert result == {}
