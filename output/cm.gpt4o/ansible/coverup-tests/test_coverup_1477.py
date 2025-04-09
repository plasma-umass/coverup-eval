# file lib/ansible/module_utils/facts/system/cmdline.py:47-66
# lines [57]
# branches ['56->57']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_list_append(cmdline_collector):
    data = 'param1=value1 param1=value2 param1=value3'
    expected_result = {
        'param1': ['value1', 'value2', 'value3']
    }
    
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    
    assert result == expected_result

def test_parse_proc_cmdline_facts_single_value(cmdline_collector):
    data = 'param1=value1 param2=value2'
    expected_result = {
        'param1': 'value1',
        'param2': 'value2'
    }
    
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    
    assert result == expected_result

def test_parse_proc_cmdline_facts_flag(cmdline_collector):
    data = 'param1=value1 flag1'
    expected_result = {
        'param1': 'value1',
        'flag1': True
    }
    
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    
    assert result == expected_result
