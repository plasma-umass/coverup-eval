# file: lib/ansible/module_utils/facts/system/cmdline.py:47-66
# asked: {"lines": [57], "branches": [[56, 57]]}
# gained: {"lines": [57], "branches": [[56, 57]]}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_single_item(cmdline_collector):
    data = "singleitem"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"singleitem": True}

def test_parse_proc_cmdline_facts_key_value(cmdline_collector):
    data = "key=value"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key": "value"}

def test_parse_proc_cmdline_facts_multiple_values_for_key(cmdline_collector):
    data = "key=value1 key=value2"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key": ["value1", "value2"]}

def test_parse_proc_cmdline_facts_mixed_items(cmdline_collector):
    data = "singleitem key=value1 key=value2 anotherkey=anothervalue"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {
        "singleitem": True,
        "key": ["value1", "value2"],
        "anotherkey": "anothervalue"
    }

def test_parse_proc_cmdline_facts_existing_key_as_list(cmdline_collector):
    data = "key=value1 key=value2 key=value3"
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    assert result == {"key": ["value1", "value2", "value3"]}
