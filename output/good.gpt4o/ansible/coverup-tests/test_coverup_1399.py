# file lib/ansible/module_utils/facts/system/platform.py:42-97
# lines [65, 66, 68, 69, 70, 71, 72]
# branches ['63->65', '65->66', '65->76', '67->68', '69->70', '69->71', '71->72', '71->76', '93->97']

import pytest
import platform
import socket
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_platform_facts():
    with patch('platform.system') as mock_system, \
         patch('platform.release') as mock_release, \
         patch('platform.version') as mock_version, \
         patch('platform.machine') as mock_machine, \
         patch('platform.python_version') as mock_python_version, \
         patch('socket.getfqdn') as mock_getfqdn, \
         patch('platform.node') as mock_node, \
         patch('platform.architecture') as mock_architecture, \
         patch('ansible.module_utils.facts.system.platform.get_file_content') as mock_get_file_content:
        
        mock_system.return_value = 'Linux'
        mock_release.return_value = '5.4.0-42-generic'
        mock_version.return_value = '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
        mock_machine.return_value = 'i686'
        mock_python_version.return_value = '3.8.5'
        mock_getfqdn.return_value = 'test.example.com'
        mock_node.return_value = 'test.example.com'
        mock_architecture.return_value = ('32bit', '')
        mock_get_file_content.return_value = '1234567890abcdef'

        yield

def test_platform_fact_collector_32bit(mock_platform_facts):
    collector = PlatformFactCollector()
    facts = collector.collect()

    assert facts['system'] == 'Linux'
    assert facts['kernel'] == '5.4.0-42-generic'
    assert facts['kernel_version'] == '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
    assert facts['machine'] == 'i686'
    assert facts['python_version'] == '3.8.5'
    assert facts['fqdn'] == 'test.example.com'
    assert facts['hostname'] == 'test'
    assert facts['nodename'] == 'test.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '32'
    assert facts['userspace_architecture'] == 'i386'
    assert facts['architecture'] == 'i386'
    assert facts['machine_id'] == '1234567890abcdef'

def test_platform_fact_collector_machine_id_none(mock_platform_facts):
    with patch('ansible.module_utils.facts.system.platform.get_file_content', return_value=None):
        collector = PlatformFactCollector()
        facts = collector.collect()

        assert 'machine_id' not in facts
