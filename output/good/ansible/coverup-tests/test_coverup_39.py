# file lib/ansible/module_utils/facts/hardware/freebsd.py:95-127
# lines [95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 118, 119, 120, 121, 122, 123, 124, 125, 127]
# branches ['99->100', '99->112', '101->102', '101->109', '103->104', '103->105', '105->106', '105->107', '107->101', '107->108', '113->118', '113->127', '120->121', '120->122', '123->124', '123->127']

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path = mocker.MagicMock(side_effect=lambda x: f"/usr/sbin/{x}")
    mock_module.run_command = mocker.MagicMock()
    return mock_module

def test_get_memory_facts(mock_module, mocker):
    sysctl_output = (
        "vm.stats.vm.v_page_size 4096\n"
        "vm.stats.vm.v_page_count 262144\n"
        "vm.stats.vm.v_free_count 131072\n"
    )
    swapinfo_output = (
        "Device          1M-blocks     Used    Avail Capacity\n"
        "/dev/ada0p3        314368        0   314368     0%\n"
    )
    mock_module.run_command.side_effect = [
        (0, sysctl_output, ''),
        (0, swapinfo_output, '')
    ]

    hardware = FreeBSDHardware(module=mock_module)
    memory_facts = hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 262144 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 131072 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368 // 1024
    assert memory_facts['swapfree_mb'] == 314368 // 1024

    mock_module.get_bin_path.assert_any_call('sysctl')
    mock_module.get_bin_path.assert_any_call('swapinfo')
    mock_module.run_command.assert_any_call("/usr/sbin/sysctl vm.stats", check_rc=False)
    mock_module.run_command.assert_any_call("/usr/sbin/swapinfo -k")
