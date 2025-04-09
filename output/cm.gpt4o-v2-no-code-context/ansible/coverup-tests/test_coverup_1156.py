# file: lib/ansible/module_utils/facts/network/fc_wwn.py:32-109
# asked: {"lines": [], "branches": [[52, 109], [59, 109], [61, 60], [67, 109], [71, 109], [74, 72], [81, 72], [83, 82], [86, 109], [90, 109], [94, 109], [97, 95], [104, 95], [106, 105]]}
# gained: {"lines": [], "branches": [[52, 109], [67, 109], [90, 109]]}

import pytest
import sys
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def mock_glob():
    with patch('glob.glob') as mock:
        yield mock

@pytest.fixture
def mock_get_file_lines():
    with patch('ansible.module_utils.facts.network.fc_wwn.get_file_lines') as mock:
        yield mock

def test_collect_linux(mock_module, mock_glob, mock_get_file_lines):
    mock_glob.return_value = ['/sys/class/fc_host/host0/port_name']
    mock_get_file_lines.return_value = ['0x21000014ff52a9bb']
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'linux'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['21000014ff52a9bb']

def test_collect_sunos_with_cmd(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/fcinfo'
    mock_module.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'sunos'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

def test_collect_sunos_without_cmd(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'sunos'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == []

def test_collect_aix_with_cmds(mock_module):
    mock_module.get_bin_path.side_effect = ['/usr/bin/lsdev', '/usr/bin/lscfg']
    mock_module.run_command.side_effect = [
        (0, 'fcs0 Available\n', ''),
        (0, 'Network Address.............10000090FA551509\n', '')
    ]
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'aix'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['10000090FA551509']

def test_collect_aix_without_cmds(mock_module):
    mock_module.get_bin_path.side_effect = [None, None]
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'aix'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == []

def test_collect_hpux_with_cmds(mock_module):
    mock_module.get_bin_path.side_effect = ['/usr/sbin/ioscan', '/opt/fcms/bin/fcmsutil']
    mock_module.run_command.side_effect = [
        (0, '/dev/fcd0\n', ''),
        (0, 'N_Port Port World Wide Name = 0x50060b00006975ec\n', '')
    ]
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'hp-ux'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['0x50060b00006975ec']

def test_collect_hpux_without_cmds(mock_module):
    mock_module.get_bin_path.side_effect = [None, None]
    collector = FcWwnInitiatorFactCollector()
    with patch('sys.platform', 'hp-ux'):
        facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == []
