# file: lib/ansible/module_utils/facts/system/cmdline.py:68-79
# asked: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}
# gained: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_collect_no_data(cmdline_collector):
    with patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._get_proc_cmdline', return_value=''):
        result = cmdline_collector.collect()
        assert result == {}

def test_collect_with_data(cmdline_collector):
    data = "BOOT_IMAGE=/vmlinuz-4.15.0-20-generic root=/dev/mapper/ubuntu--vg-root ro quiet splash"
    with patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._get_proc_cmdline', return_value=data):
        with patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._parse_proc_cmdline', return_value={'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic', 'root': '/dev/mapper/ubuntu--vg-root', 'ro': True, 'quiet': True, 'splash': True}):
            with patch('ansible.module_utils.facts.system.cmdline.CmdLineFactCollector._parse_proc_cmdline_facts', return_value={'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic', 'root': '/dev/mapper/ubuntu--vg-root', 'ro': True, 'quiet': True, 'splash': True}):
                result = cmdline_collector.collect()
                assert result == {
                    'cmdline': {'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic', 'root': '/dev/mapper/ubuntu--vg-root', 'ro': True, 'quiet': True, 'splash': True},
                    'proc_cmdline': {'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic', 'root': '/dev/mapper/ubuntu--vg-root', 'ro': True, 'quiet': True, 'splash': True}
                }

def test_parse_proc_cmdline():
    data = "BOOT_IMAGE=/vmlinuz-4.15.0-20-generic root=/dev/mapper/ubuntu--vg-root ro quiet splash"
    collector = CmdLineFactCollector()
    result = collector._parse_proc_cmdline(data)
    assert result == {
        'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic',
        'root': '/dev/mapper/ubuntu--vg-root',
        'ro': True,
        'quiet': True,
        'splash': True
    }

def test_parse_proc_cmdline_facts():
    data = "BOOT_IMAGE=/vmlinuz-4.15.0-20-generic root=/dev/mapper/ubuntu--vg-root ro quiet splash"
    collector = CmdLineFactCollector()
    result = collector._parse_proc_cmdline_facts(data)
    assert result == {
        'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic',
        'root': '/dev/mapper/ubuntu--vg-root',
        'ro': True,
        'quiet': True,
        'splash': True
    }
