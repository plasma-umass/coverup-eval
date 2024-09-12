# file: lib/ansible/module_utils/facts/hardware/aix.py:57-84
# asked: {"lines": [58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84], "branches": [[62, 63], [62, 84], [64, 66], [64, 72], [66, 64], [66, 67], [67, 68], [67, 71], [80, 81], [80, 84]]}
# gained: {"lines": [58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84], "branches": [[62, 63], [64, 66], [64, 72], [66, 67], [67, 68], [67, 71], [80, 81]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

def test_get_cpu_facts(mock_module):
    aix_hardware = AIXHardware(mock_module)

    # Mock the run_command method
    def mock_run_command(cmd):
        if cmd == "/usr/sbin/lsdev -Cc processor":
            return (0, "proc0 Available\nproc1 Available\n", "")
        elif cmd.startswith("/usr/sbin/lsattr -El proc0 -a type"):
            return (0, "type PowerPC_POWER8", "")
        elif cmd.startswith("/usr/sbin/lsattr -El proc0 -a smt_threads"):
            return (0, "smt_threads 8", "")
        return (1, "", "Error")

    mock_module.run_command.side_effect = mock_run_command

    cpu_facts = aix_hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_cores'] == 8
