# file: lib/ansible/module_utils/facts/system/cmdline.py:68-79
# asked: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}
# gained: {"lines": [68, 69, 71, 73, 74, 76, 77, 79], "branches": [[73, 74], [73, 76]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

@pytest.fixture
def cmdline_collector():
    return CmdLineFactCollector()

def test_collect_no_data(cmdline_collector):
    with patch.object(cmdline_collector, '_get_proc_cmdline', return_value=''):
        result = cmdline_collector.collect()
        assert result == {}

def test_collect_with_data(cmdline_collector):
    mock_data = "BOOT_IMAGE=/vmlinuz-5.4.0-42-generic root=/dev/sda1 ro quiet splash"
    with patch.object(cmdline_collector, '_get_proc_cmdline', return_value=mock_data):
        with patch.object(cmdline_collector, '_parse_proc_cmdline', return_value={'BOOT_IMAGE': '/vmlinuz-5.4.0-42-generic', 'root': '/dev/sda1', 'ro': True, 'quiet': True, 'splash': True}):
            with patch.object(cmdline_collector, '_parse_proc_cmdline_facts', return_value={'BOOT_IMAGE': '/vmlinuz-5.4.0-42-generic', 'root': '/dev/sda1', 'ro': True, 'quiet': True, 'splash': True}):
                result = cmdline_collector.collect()
                assert 'cmdline' in result
                assert 'proc_cmdline' in result
                assert result['cmdline'] == {'BOOT_IMAGE': '/vmlinuz-5.4.0-42-generic', 'root': '/dev/sda1', 'ro': True, 'quiet': True, 'splash': True}
                assert result['proc_cmdline'] == {'BOOT_IMAGE': '/vmlinuz-5.4.0-42-generic', 'root': '/dev/sda1', 'ro': True, 'quiet': True, 'splash': True}
