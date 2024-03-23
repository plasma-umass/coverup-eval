# file lib/ansible/module_utils/facts/system/cmdline.py:68-79
# lines [68, 69, 71, 73, 74, 76, 77, 79]
# branches ['73->74', '73->76']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def mock_get_proc_cmdline(mocker):
    mocker.patch.object(CmdLineFactCollector, '_get_proc_cmdline', return_value="root=/dev/sda1 ro")

@pytest.fixture
def mock_parse_proc_cmdline(mocker):
    mocker.patch.object(CmdLineFactCollector, '_parse_proc_cmdline', return_value={'root': '/dev/sda1', 'ro': True})

@pytest.fixture
def mock_parse_proc_cmdline_facts(mocker):
    mocker.patch.object(CmdLineFactCollector, '_parse_proc_cmdline_facts', return_value={'ROOT': '/dev/sda1', 'RO': True})

def test_collect_cmdline_facts(mock_get_proc_cmdline, mock_parse_proc_cmdline, mock_parse_proc_cmdline_facts):
    collector = CmdLineFactCollector()
    facts = collector.collect()

    assert 'cmdline' in facts
    assert facts['cmdline'] == {'root': '/dev/sda1', 'ro': True}
    assert 'proc_cmdline' in facts
    assert facts['proc_cmdline'] == {'ROOT': '/dev/sda1', 'RO': True}

def test_collect_cmdline_facts_empty(mock_get_proc_cmdline, mock_parse_proc_cmdline, mock_parse_proc_cmdline_facts):
    CmdLineFactCollector._get_proc_cmdline.return_value = ""
    collector = CmdLineFactCollector()
    facts = collector.collect()

    assert 'cmdline' not in facts
    assert 'proc_cmdline' not in facts
    assert facts == {}
