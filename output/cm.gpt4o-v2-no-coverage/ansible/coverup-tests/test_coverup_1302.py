# file: lib/ansible/module_utils/facts/system/cmdline.py:33-45
# asked: {"lines": [42, 43], "branches": []}
# gained: {"lines": [42, 43], "branches": []}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_empty_string(cmdline_collector):
    result = cmdline_collector._parse_proc_cmdline("")
    assert result == {}

def test_parse_proc_cmdline_single_flag(cmdline_collector):
    result = cmdline_collector._parse_proc_cmdline("single_flag")
    assert result == {"single_flag": True}

def test_parse_proc_cmdline_key_value_pair(cmdline_collector):
    result = cmdline_collector._parse_proc_cmdline("key=value")
    assert result == {"key": "value"}

def test_parse_proc_cmdline_multiple_pairs(cmdline_collector):
    result = cmdline_collector._parse_proc_cmdline("key1=value1 key2=value2")
    assert result == {"key1": "value1", "key2": "value2"}

def test_parse_proc_cmdline_mixed_pairs(cmdline_collector):
    result = cmdline_collector._parse_proc_cmdline("key1=value1 single_flag key2=value2")
    assert result == {"key1": "value1", "single_flag": True, "key2": "value2"}

def test_parse_proc_cmdline_value_error(cmdline_collector, monkeypatch):
    def mock_split(data, posix):
        raise ValueError("mocked error")
    monkeypatch.setattr("shlex.split", mock_split)
    result = cmdline_collector._parse_proc_cmdline("key=value")
    assert result == {}
