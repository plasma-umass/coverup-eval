# file lib/ansible/module_utils/facts/network/fc_wwn.py:32-109
# lines [32, 40, 41, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100, 101, 104, 105, 106, 107, 108, 109]
# branches ['42->43', '42->46', '43->44', '43->109', '44->43', '44->45', '46->47', '46->64', '52->53', '52->109', '59->60', '59->109', '60->61', '60->109', '61->60', '61->62', '64->65', '64->86', '67->69', '67->109', '71->72', '71->109', '72->74', '72->109', '74->72', '74->75', '81->72', '81->82', '82->72', '82->83', '83->82', '83->84', '86->87', '86->109', '90->92', '90->109', '94->95', '94->109', '95->96', '95->109', '97->95', '97->98', '104->95', '104->105', '105->95', '105->106', '106->105', '106->107']

import pytest
import sys
from unittest.mock import patch, mock_open, MagicMock
from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda cmd, opt_dirs=None: f"/usr/bin/{cmd}" if cmd in ['fcinfo', 'lsdev', 'lscfg', 'ioscan', 'fcmsutil'] else None
    return module

@pytest.fixture
def mock_glob():
    with patch('glob.glob') as mock_glob:
        yield mock_glob

@pytest.fixture
def mock_get_file_lines():
    with patch('ansible.module_utils.facts.network.fc_wwn.get_file_lines') as mock_get_file_lines:
        yield mock_get_file_lines

@pytest.mark.parametrize("platform, fc_files, file_lines, cmd_output, expected_wwn", [
    ('linux', ['/sys/class/fc_host/host0/port_name'], ['0x21000014ff52a9bb'], None, ['21000014ff52a9bb']),
    ('sunos', [], [], "HBA Port WWN: 10000090fa1658de\n", ['10000090fa1658de']),
    ('aix', [], [], "fcs0 Available\n", ['10000090FA551509']),
    ('hp-ux', [], [], "/dev/fcd0\n", ['0x50060b00006975ec']),
])
def test_fc_wwn_initiator_fact_collector(mock_module, mock_glob, mock_get_file_lines, platform, fc_files, file_lines, cmd_output, expected_wwn):
    collector = FcWwnInitiatorFactCollector()
    
    with patch('sys.platform', platform):
        if platform == 'linux':
            mock_glob.return_value = fc_files
            mock_get_file_lines.return_value = file_lines
        elif platform == 'sunos':
            mock_module.run_command.return_value = (0, cmd_output, '')
        elif platform == 'aix':
            mock_module.run_command.side_effect = [
                (0, cmd_output, ''),  # lsdev output
                (0, "Network Address.............10000090FA551509\n", '')  # lscfg output
            ]
        elif platform == 'hp-ux':
            mock_module.run_command.side_effect = [
                (0, cmd_output, ''),  # ioscan output
                (0, "N_Port Port World Wide Name = 0x50060b00006975ec\n", '')  # fcmsutil output
            ]

        facts = collector.collect(module=mock_module)
        assert 'fibre_channel_wwn' in facts
        assert facts['fibre_channel_wwn'] == expected_wwn
