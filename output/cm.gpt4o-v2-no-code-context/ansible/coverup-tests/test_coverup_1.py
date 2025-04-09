# file: lib/ansible/module_utils/facts/network/fc_wwn.py:32-109
# asked: {"lines": [32, 40, 41, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100, 101, 104, 105, 106, 107, 108, 109], "branches": [[42, 43], [42, 46], [43, 44], [43, 109], [44, 43], [44, 45], [46, 47], [46, 64], [52, 53], [52, 109], [59, 60], [59, 109], [60, 61], [60, 109], [61, 60], [61, 62], [64, 65], [64, 86], [67, 69], [67, 109], [71, 72], [71, 109], [72, 74], [72, 109], [74, 72], [74, 75], [81, 72], [81, 82], [82, 72], [82, 83], [83, 82], [83, 84], [86, 87], [86, 109], [90, 92], [90, 109], [94, 95], [94, 109], [95, 96], [95, 109], [97, 95], [97, 98], [104, 95], [104, 105], [105, 95], [105, 106], [106, 105], [106, 107]]}
# gained: {"lines": [32, 40, 41, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100, 101, 104, 105, 106, 107, 108, 109], "branches": [[42, 43], [42, 46], [43, 44], [43, 109], [44, 43], [44, 45], [46, 47], [46, 64], [52, 53], [59, 60], [60, 61], [60, 109], [61, 62], [64, 65], [64, 86], [67, 69], [71, 72], [72, 74], [72, 109], [74, 75], [81, 82], [82, 72], [82, 83], [83, 84], [86, 87], [90, 92], [94, 95], [95, 96], [95, 109], [97, 98], [104, 105], [105, 95], [105, 106], [106, 107]]}

import pytest
import sys
from unittest.mock import MagicMock, patch

# Assuming the FcWwnInitiatorFactCollector and BaseFactCollector are imported from the module
from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def collector():
    return FcWwnInitiatorFactCollector()

def test_collect_linux(monkeypatch, collector, module_mock):
    monkeypatch.setattr(sys, 'platform', 'linux')
    mock_glob = MagicMock(return_value=['/sys/class/fc_host/host0/port_name'])
    mock_get_file_lines = MagicMock(return_value=['0x21000014ff52a9bb\n'])
    
    monkeypatch.setattr('glob.glob', mock_glob)
    monkeypatch.setattr('ansible.module_utils.facts.network.fc_wwn.get_file_lines', mock_get_file_lines)
    
    result = collector.collect(module=module_mock)
    
    assert result == {'fibre_channel_wwn': ['21000014ff52a9bb']}
    mock_glob.assert_called_once_with('/sys/class/fc_host/*/port_name')
    mock_get_file_lines.assert_called_once_with('/sys/class/fc_host/host0/port_name')

def test_collect_sunos(monkeypatch, collector, module_mock):
    monkeypatch.setattr(sys, 'platform', 'sunos')
    module_mock.get_bin_path.return_value = '/usr/bin/fcinfo'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')
    
    result = collector.collect(module=module_mock)
    
    assert result == {'fibre_channel_wwn': ['10000090fa1658de']}
    module_mock.get_bin_path.assert_called_once_with('fcinfo')
    module_mock.run_command.assert_called_once_with('/usr/bin/fcinfo hba-port')

def test_collect_aix(monkeypatch, collector, module_mock):
    monkeypatch.setattr(sys, 'platform', 'aix')
    module_mock.get_bin_path.side_effect = ['/usr/bin/lsdev', '/usr/bin/lscfg']
    module_mock.run_command.side_effect = [
        (0, 'fcs0 Available 00-00\n', ''),
        (0, 'Network Address.............10000090FA551509\n', '')
    ]
    
    result = collector.collect(module=module_mock)
    
    assert result == {'fibre_channel_wwn': ['10000090FA551509']}
    module_mock.get_bin_path.assert_any_call('lsdev')
    module_mock.get_bin_path.assert_any_call('lscfg')
    module_mock.run_command.assert_any_call('/usr/bin/lsdev -Cc adapter -l fcs*')
    module_mock.run_command.assert_any_call('/usr/bin/lscfg -vl fcs0')

def test_collect_hpux(monkeypatch, collector, module_mock):
    monkeypatch.setattr(sys, 'platform', 'hp-ux')
    module_mock.get_bin_path.side_effect = ['/usr/sbin/ioscan', '/opt/fcms/bin/fcmsutil']
    module_mock.run_command.side_effect = [
        (0, '/dev/fcd0\n', ''),
        (0, 'N_Port Port World Wide Name = 0x50060b00006975ec\n', '')
    ]
    
    result = collector.collect(module=module_mock)
    
    assert result == {'fibre_channel_wwn': ['0x50060b00006975ec']}
    module_mock.get_bin_path.assert_any_call('ioscan')
    module_mock.get_bin_path.assert_any_call('fcmsutil', opt_dirs=['/opt/fcms/bin'])
    module_mock.run_command.assert_any_call('/usr/sbin/ioscan -fnC FC')
    module_mock.run_command.assert_any_call('/opt/fcms/bin/fcmsutil /dev/fcd0')
