# file: lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# asked: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}
# gained: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}

import pytest
import struct
import time
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mocker, mock_module):
    hardware = FreeBSDHardware(module=mock_module)

    # Mock the run_command to return a successful response
    mock_module.run_command.return_value = (0, struct.pack('@L', int(time.time()) - 1000), '')

    result = hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] >= 1000

def test_get_uptime_facts_failure_sysctl_not_found(mocker, mock_module):
    hardware = FreeBSDHardware(module=mock_module)

    # Mock the get_bin_path to return None
    mock_module.get_bin_path.return_value = None

    # Mock the run_command to return a default response
    mock_module.run_command.return_value = (0, b'', '')

    result = hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_failure_run_command(mocker, mock_module):
    hardware = FreeBSDHardware(module=mock_module)

    # Mock the run_command to return a failure response
    mock_module.run_command.return_value = (1, b'', 'error')

    result = hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_failure_short_output(mocker, mock_module):
    hardware = FreeBSDHardware(module=mock_module)

    # Mock the run_command to return a short output
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = hardware.get_uptime_facts()

    assert result == {}
