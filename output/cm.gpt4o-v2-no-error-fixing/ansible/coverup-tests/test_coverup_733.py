# file: lib/ansible/module_utils/facts/system/cmdline.py:47-66
# asked: {"lines": [48, 49, 50, 51, 52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66], "branches": [[50, 51], [50, 66], [52, 53], [52, 55], [55, 56], [55, 62], [56, 57], [56, 59]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 55, 56, 59, 60, 62, 63, 64, 66], "branches": [[50, 51], [50, 66], [52, 53], [52, 55], [55, 56], [55, 62], [56, 59]]}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_fact_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_single_item(cmdline_fact_collector):
    data = "single_item"
    expected_result = {"single_item": True}
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)
    assert result == expected_result

def test_parse_proc_cmdline_facts_key_value_pair(cmdline_fact_collector):
    data = "key=value"
    expected_result = {"key": "value"}
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)
    assert result == expected_result

def test_parse_proc_cmdline_facts_multiple_values_for_key(cmdline_fact_collector):
    data = "key=value1 key=value2"
    expected_result = {"key": ["value1", "value2"]}
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)
    assert result == expected_result

def test_parse_proc_cmdline_facts_mixed_items(cmdline_fact_collector):
    data = "key1=value1 key2 key1=value2"
    expected_result = {"key1": ["value1", "value2"], "key2": True}
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)
    assert result == expected_result

def test_parse_proc_cmdline_facts_value_error(cmdline_fact_collector, monkeypatch):
    def mock_shlex_split(data, posix):
        raise ValueError("mocked error")
    monkeypatch.setattr("shlex.split", mock_shlex_split)
    data = "key=value"
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)
    assert result == {}
