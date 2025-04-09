# file: lib/ansible/module_utils/facts/system/cmdline.py:47-66
# asked: {"lines": [57, 63, 64], "branches": [[56, 57]]}
# gained: {"lines": [63, 64], "branches": []}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_single_value(cmdline_collector):
    data = "key1=value1"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": "value1"}

def test_parse_proc_cmdline_facts_multiple_values(cmdline_collector):
    data = "key1=value1 key1=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": ["value1", "value2"]}

def test_parse_proc_cmdline_facts_no_value(cmdline_collector):
    data = "key1"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": True}

def test_parse_proc_cmdline_facts_mixed_values(cmdline_collector):
    data = "key1=value1 key2 key1=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": ["value1", "value2"], "key2": True}

def test_parse_proc_cmdline_facts_value_error(cmdline_collector, monkeypatch):
    def mock_shlex_split(data, posix):
        raise ValueError("mocked error")
    
    monkeypatch.setattr("shlex.split", mock_shlex_split)
    data = "key1=value1"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {}
