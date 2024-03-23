# file lib/ansible/module_utils/facts/system/cmdline.py:47-66
# lines [48, 49, 50, 51, 52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66]
# branches ['50->51', '50->66', '52->53', '52->55', '55->56', '55->62', '56->57', '56->59']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmd_line_fact_collector():
    return CmdLineFactCollector()

def test_parse_proc_cmdline_facts_with_multiple_values_for_same_key(cmd_line_fact_collector):
    data = 'key1=value1 key1=value2 key2=value3 key3 key4=value4 key4=value5 key4=value6'
    expected_result = {
        'key1': ['value1', 'value2'],
        'key2': 'value3',
        'key3': True,
        'key4': ['value4', 'value5', 'value6']
    }
    result = cmd_line_fact_collector._parse_proc_cmdline_facts(data)
    assert result == expected_result

def test_parse_proc_cmdline_facts_with_invalid_shlex_data(cmd_line_fact_collector, mocker):
    mocker.patch('shlex.split', side_effect=ValueError)
    data = 'key1="value1 value2" key2=value3'
    result = cmd_line_fact_collector._parse_proc_cmdline_facts(data)
    assert result == {}
