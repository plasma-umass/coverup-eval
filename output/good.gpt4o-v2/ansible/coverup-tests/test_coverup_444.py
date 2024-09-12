# file: lib/ansible/module_utils/facts/system/cmdline.py:68-79
# asked: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}
# gained: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_fact_collector():
    return CmdLineFactCollector()

def test_collect_no_data(cmdline_fact_collector):
    with patch.object(cmdline_fact_collector, '_get_proc_cmdline', return_value=''):
        result = cmdline_fact_collector.collect()
        assert result == {}

def test_collect_with_data(cmdline_fact_collector):
    data = 'root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/swap'
    with patch.object(cmdline_fact_collector, '_get_proc_cmdline', return_value=data):
        with patch.object(cmdline_fact_collector, '_parse_proc_cmdline', return_value={'root': '/dev/mapper/centos-root'}):
            with patch.object(cmdline_fact_collector, '_parse_proc_cmdline_facts', return_value={'crashkernel': 'auto'}):
                result = cmdline_fact_collector.collect()
                assert result == {
                    'cmdline': {'root': '/dev/mapper/centos-root'},
                    'proc_cmdline': {'crashkernel': 'auto'}
                }
