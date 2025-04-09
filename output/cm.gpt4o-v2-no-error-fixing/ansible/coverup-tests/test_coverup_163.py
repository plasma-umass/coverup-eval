# file: lib/ansible/module_utils/facts/hardware/openbsd.py:114-130
# asked: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}
# gained: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}

import pytest
import time
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mock_module):
    openbsd_hw = OpenBSDHardware(mock_module)
    mock_module.run_command.return_value = (0, '1633072800\n', '')

    with patch('time.time', return_value=1633076400):
        result = openbsd_hw.get_uptime_facts()

    assert result == {'uptime_seconds': 3600}

def test_get_uptime_facts_sysctl_failure(mock_module):
    openbsd_hw = OpenBSDHardware(mock_module)
    mock_module.run_command.return_value = (1, '', 'error')

    result = openbsd_hw.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_non_digit_boottime(mock_module):
    openbsd_hw = OpenBSDHardware(mock_module)
    mock_module.run_command.return_value = (0, 'invalid\n', '')

    result = openbsd_hw.get_uptime_facts()

    assert result == {}
