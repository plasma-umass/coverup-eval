# file lib/ansible/module_utils/facts/system/cmdline.py:47-66
# lines [48, 49, 50, 51, 52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66]
# branches ['50->51', '50->66', '52->53', '52->55', '55->56', '55->62', '56->57', '56->59']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts(cmdline_collector):
    # Test case to cover the lines 48-66
    data = 'param1=value1 param2=value2 param3 param4=value4 param4=value5'
    
    expected_result = {
        'param1': 'value1',
        'param2': 'value2',
        'param3': True,
        'param4': ['value4', 'value5']
    }
    
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    
    assert result == expected_result

def test_parse_proc_cmdline_facts_with_value_error(cmdline_collector, mocker):
    # Mock shlex.split to raise ValueError
    mocker.patch('shlex.split', side_effect=ValueError)
    
    data = 'param1=value1'
    
    result = cmdline_collector._parse_proc_cmdline_facts(data)
    
    assert result == {}
