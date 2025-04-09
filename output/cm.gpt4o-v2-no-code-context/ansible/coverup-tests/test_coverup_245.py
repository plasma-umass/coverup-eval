# file: lib/ansible/module_utils/facts/hardware/openbsd.py:114-130
# asked: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}
# gained: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}

import pytest
import time
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mocker, mock_module):
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.time.time', return_value=1000000)
    mock_module.run_command.return_value = (0, '500000', '')

    hardware = OpenBSDHardware(mock_module)

    result = hardware.get_uptime_facts()
    assert result == {'uptime_seconds': 500000}

def test_get_uptime_facts_sysctl_failure(mocker, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')

    hardware = OpenBSDHardware(mock_module)

    result = hardware.get_uptime_facts()
    assert result == {}

def test_get_uptime_facts_non_digit_boottime(mocker, mock_module):
    mock_module.run_command.return_value = (0, 'not_a_digit', '')

    hardware = OpenBSDHardware(mock_module)

    result = hardware.get_uptime_facts()
    assert result == {}
