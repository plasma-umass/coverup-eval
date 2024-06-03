# file lib/ansible/module_utils/facts/hardware/sunos.py:122-143
# lines [122, 123, 125, 127, 128, 129, 131, 133, 134, 135, 136, 138, 139, 140, 141, 143]
# branches ['127->128', '127->131', '128->127', '128->129']

import pytest
from unittest.mock import Mock

# Assuming the SunOSHardware class is imported from ansible.module_utils.facts.hardware.sunos
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

class TestSunOSHardware:
    @pytest.fixture
    def mock_module(self, mocker):
        module = Mock()
        mocker.patch.object(module, 'run_command')
        return module

    def test_get_memory_facts(self, mock_module):
        # Mock the output of the prtconf command
        mock_module.run_command.side_effect = [
            (0, "System Configuration:  Oracle Corporation  sun4v\nMemory size: 16384 Megabytes", ""),
            (0, "total: 4194304k bytes allocated + 2048k reserved = 4196352k used, 1048576k available", "")
        ]

        hardware = SunOSHardware(module=mock_module)

        memory_facts = hardware.get_memory_facts()

        assert memory_facts['memtotal_mb'] == 16384
        assert memory_facts['swapfree_mb'] == 1024
        assert memory_facts['swaptotal_mb'] == (4196352 + 1048576) // 1024
        assert memory_facts['swap_allocated_mb'] == 4194304 // 1024
        assert memory_facts['swap_reserved_mb'] == 2048 // 1024

        # Ensure the run_command was called with the expected commands
        mock_module.run_command.assert_any_call(["/usr/sbin/prtconf"])
        mock_module.run_command.assert_any_call("/usr/sbin/swap -s")
