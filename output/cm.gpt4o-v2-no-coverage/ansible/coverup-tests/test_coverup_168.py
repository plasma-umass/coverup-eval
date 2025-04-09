# file: lib/ansible/module_utils/facts/system/cmdline.py:47-66
# asked: {"lines": [47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66], "branches": [[50, 51], [50, 66], [52, 53], [52, 55], [55, 56], [55, 62], [56, 57], [56, 59]]}
# gained: {"lines": [47, 48, 49, 50, 51, 52, 53, 55, 56, 59, 60, 62, 66], "branches": [[50, 51], [50, 66], [52, 53], [52, 55], [55, 56], [55, 62], [56, 59]]}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_single_key(cmdline_collector):
    data = "key1"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": True}

def test_parse_proc_cmdline_facts_key_value(cmdline_collector):
    data = "key1=value1"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": "value1"}

def test_parse_proc_cmdline_facts_multiple_keys(cmdline_collector):
    data = "key1=value1 key2=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": "value1", "key2": "value2"}

def test_parse_proc_cmdline_facts_duplicate_keys(cmdline_collector):
    data = "key1=value1 key1=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": ["value1", "value2"]}

def test_parse_proc_cmdline_facts_mixed_keys(cmdline_collector):
    data = "key1=value1 key2 key1=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": ["value1", "value2"], "key2": True}

def test_parse_proc_cmdline_facts_invalid_data(cmdline_collector):
    data = "key1=value1 key2=\"unclosed_quote"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key1": "value1", "key2": "\"unclosed_quote"}

