# file: lib/ansible/module_utils/facts/system/cmdline.py:68-79
# asked: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}
# gained: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def cmdline_fact_collector():
    return CmdLineFactCollector()

def test_collect_no_data(monkeypatch, cmdline_fact_collector):
    def mock_get_proc_cmdline():
        return None

    monkeypatch.setattr(cmdline_fact_collector, '_get_proc_cmdline', mock_get_proc_cmdline)
    result = cmdline_fact_collector.collect()
    assert result == {}

def test_collect_with_data(monkeypatch, cmdline_fact_collector):
    def mock_get_proc_cmdline():
        return "root=/dev/mapper/centos-root ro"

    def mock_parse_proc_cmdline(data):
        return data.split()

    def mock_parse_proc_cmdline_facts(data):
        return {'root': '/dev/mapper/centos-root', 'ro': None}

    monkeypatch.setattr(cmdline_fact_collector, '_get_proc_cmdline', mock_get_proc_cmdline)
    monkeypatch.setattr(cmdline_fact_collector, '_parse_proc_cmdline', mock_parse_proc_cmdline)
    monkeypatch.setattr(cmdline_fact_collector, '_parse_proc_cmdline_facts', mock_parse_proc_cmdline_facts)

    result = cmdline_fact_collector.collect()
    assert result == {
        'cmdline': ['root=/dev/mapper/centos-root', 'ro'],
        'proc_cmdline': {'root': '/dev/mapper/centos-root', 'ro': None}
    }
