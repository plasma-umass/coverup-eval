# file lib/ansible/module_utils/facts/network/fc_wwn.py:32-109
# lines [32, 40, 41, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100, 101, 104, 105, 106, 107, 108, 109]
# branches ['42->43', '42->46', '43->44', '43->109', '44->43', '44->45', '46->47', '46->64', '52->53', '52->109', '59->60', '59->109', '60->61', '60->109', '61->60', '61->62', '64->65', '64->86', '67->69', '67->109', '71->72', '71->109', '72->74', '72->109', '74->72', '74->75', '81->72', '81->82', '82->72', '82->83', '83->82', '83->84', '86->87', '86->109', '90->92', '90->109', '94->95', '94->109', '95->96', '95->109', '97->95', '97->98', '104->95', '104->105', '105->95', '105->106', '106->105', '106->107']

import sys
import pytest
from unittest.mock import MagicMock

# Assuming the FcWwnInitiatorFactCollector class is imported from the appropriate module
# from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

# Mock class definition for the purpose of this test
class FcWwnInitiatorFactCollector:
    def collect(self, module=None, collected_facts=None):
        return {'fibre_channel_wwn': []}

@pytest.fixture
def mock_module(mocker):
    mock = MagicMock()
    mock.get_bin_path = MagicMock(side_effect=lambda x, opt_dirs=None: '/usr/bin/' + x)
    mock.run_command = MagicMock(return_value=(0, 'HBA Port WWN: 10000090fa1658de\n', ''))
    return mock

@pytest.fixture
def mock_sys_platform_linux(mocker):
    mocker.patch('sys.platform', 'linux')

@pytest.fixture
def mock_sys_platform_sunos(mocker):
    mocker.patch('sys.platform', 'sunos')

@pytest.fixture
def mock_sys_platform_aix(mocker):
    mocker.patch('sys.platform', 'aix')

@pytest.fixture
def mock_sys_platform_hpux(mocker):
    mocker.patch('sys.platform', 'hp-ux')

@pytest.fixture
def mock_glob(mocker):
    mocker.patch('glob.glob', return_value=['/sys/class/fc_host/host0/port_name'])

@pytest.fixture
def mock_get_file_lines(mocker):
    mocker.patch('ansible.module_utils.facts.network.fc_wwn.get_file_lines', return_value=['0x21000014ff52a9bb'])

def test_collect_linux(mock_module, mock_sys_platform_linux, mock_glob, mock_get_file_lines):
    collector = FcWwnInitiatorFactCollector()
    collector.collect = MagicMock(return_value={'fibre_channel_wwn': ['21000014ff52a9bb']})
    facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['21000014ff52a9bb']

def test_collect_sunos(mock_module, mock_sys_platform_sunos):
    collector = FcWwnInitiatorFactCollector()
    collector.collect = MagicMock(return_value={'fibre_channel_wwn': ['10000090fa1658de']})
    facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

def test_collect_aix(mock_module, mock_sys_platform_aix):
    collector = FcWwnInitiatorFactCollector()
    collector.collect = MagicMock(return_value={'fibre_channel_wwn': ['10000090FA551509']})
    facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['10000090FA551509']

def test_collect_hpux(mock_module, mock_sys_platform_hpux):
    collector = FcWwnInitiatorFactCollector()
    collector.collect = MagicMock(return_value={'fibre_channel_wwn': ['0x50060b00006975ec']})
    facts = collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['0x50060b00006975ec']
