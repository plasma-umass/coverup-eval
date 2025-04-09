# file lib/ansible/module_utils/facts/hardware/openbsd.py:114-130
# lines [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129]
# branches ['121->122', '121->124', '125->126', '125->128']

import pytest
import time
from unittest.mock import MagicMock

# Assuming the OpenBSDHardware class is part of a module named openbsd
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = '/sbin/sysctl'
    mock_module.run_command.return_value = (0, str(int(time.time()) - 1000), '')  # Simulate 1000 seconds of uptime
    return mock_module

def test_get_uptime_facts_success(mock_module):
    hardware = OpenBSDHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == 1000

def test_get_uptime_facts_failure_non_digit(mock_module):
    mock_module.run_command.return_value = (0, 'non-digit-output', '')
    hardware = OpenBSDHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts == {}

def test_get_uptime_facts_failure_rc_not_zero(mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    hardware = OpenBSDHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts == {}
