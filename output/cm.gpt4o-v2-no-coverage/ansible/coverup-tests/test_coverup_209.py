# file: lib/ansible/module_utils/facts/hardware/sunos.py:122-143
# asked: {"lines": [122, 123, 125, 127, 128, 129, 131, 133, 134, 135, 136, 138, 139, 140, 141, 143], "branches": [[127, 128], [127, 131], [128, 127], [128, 129]]}
# gained: {"lines": [122, 123, 125, 127, 128, 129, 131, 133, 134, 135, 136, 138, 139, 140, 141, 143], "branches": [[127, 128], [127, 131], [128, 127], [128, 129]]}

import pytest
from unittest.mock import Mock

from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def module():
    return Mock()

@pytest.fixture
def sunos_hardware(module):
    return SunOSHardware(module)

def test_get_memory_facts_prtconf(monkeypatch, sunos_hardware):
    prtconf_output = "System Configuration:  Oracle Corporation  sun4v\nMemory size: 16384 Megabytes\n"
    swap_output = "total: 4194304k bytes allocated + 2097152k reserved = 6291456k used, 1048576k available"

    def mock_run_command(cmd):
        if cmd == ["/usr/sbin/prtconf"]:
            return 0, prtconf_output, ""
        elif cmd == "/usr/sbin/swap -s":
            return 0, swap_output, ""
        return 1, "", "Command not found"

    monkeypatch.setattr(sunos_hardware.module, 'run_command', mock_run_command)

    memory_facts = sunos_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 16384
    assert memory_facts['swapfree_mb'] == 1024
    assert memory_facts['swaptotal_mb'] == 7168
    assert memory_facts['swap_allocated_mb'] == 4096
    assert memory_facts['swap_reserved_mb'] == 2048
