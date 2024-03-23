# file lib/ansible/module_utils/facts/hardware/sunos.py:122-143
# lines [122, 123, 125, 127, 128, 129, 131, 133, 134, 135, 136, 138, 139, 140, 141, 143]
# branches ['127->128', '127->131', '128->127', '128->129']

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock()
    module_mock.run_command = mocker.MagicMock()
    return module_mock

def test_get_memory_facts(mock_module):
    sunos_hardware = SunOSHardware(mock_module)

    # Mock the output of the commands
    mock_module.run_command.side_effect = [
        (0, "Memory size: 8192 Megabytes", ""),
        (0, "total: 178488k bytes allocated + 62960k reserved = 241448k used, 1188728k available", "")
    ]

    expected_memory_facts = {
        'memtotal_mb': 8192,
        'swapfree_mb': 1188728 // 1024,
        'swaptotal_mb': (1188728 + 241448) // 1024,
        'swap_allocated_mb': 178488 // 1024,
        'swap_reserved_mb': 62960 // 1024
    }

    memory_facts = sunos_hardware.get_memory_facts()

    assert memory_facts == expected_memory_facts
    assert mock_module.run_command.call_count == 2
    mock_module.run_command.assert_any_call(["/usr/sbin/prtconf"])
    mock_module.run_command.assert_any_call("/usr/sbin/swap -s")
