# file: lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# asked: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}
# gained: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}

import pytest
from unittest.mock import Mock, patch
import time
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_get_uptime_facts_success(sunos_hardware, mock_module):
    mock_module.run_command.return_value = (0, "unix:0:system_misc:boot_time\t1548249689", "")
    current_time = 1548253289  # Mock current time for consistency
    with patch('time.time', return_value=current_time):
        uptime_facts = sunos_hardware.get_uptime_facts()
        assert uptime_facts['uptime_seconds'] == current_time - 1548249689

def test_get_uptime_facts_failure(sunos_hardware, mock_module):
    mock_module.run_command.return_value = (1, "", "error")
    uptime_facts = sunos_hardware.get_uptime_facts()
    assert uptime_facts is None
