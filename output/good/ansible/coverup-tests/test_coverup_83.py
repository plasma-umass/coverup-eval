# file lib/ansible/module_utils/facts/hardware/freebsd.py:71-93
# lines [71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 93]
# branches ['75->76', '75->79', '80->81', '80->86', '86->87', '86->93', '87->88', '87->90', '90->86', '90->91']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/sbin/' + x)
    mock_module.run_command = MagicMock()
    return mock_module

@pytest.fixture
def mock_get_file_content(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=None)

def test_get_cpu_facts(mock_module, mock_get_file_content):
    hardware = FreeBSDHardware(module=mock_module)
    mock_module.run_command.side_effect = [
        (0, '4', ''),  # Mock sysctl -n hw.ncpu
        (0, 'CPU: Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz (2712.00-MHz K8-class CPU)\nLogical CPUs per core: 2', '')  # Mock dmesg
    ]

    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor'] == ['Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz (2712.00-MHz K8-class CPU)']
    assert cpu_facts['processor_cores'] == '2'
    mock_module.get_bin_path.assert_any_call('sysctl')
    mock_module.get_bin_path.assert_any_call('dmesg')
    mock_module.run_command.assert_any_call('/usr/sbin/sysctl -n hw.ncpu', check_rc=False)
    mock_module.run_command.assert_any_call('/usr/sbin/dmesg', check_rc=False)
