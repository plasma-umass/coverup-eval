# file lib/ansible/module_utils/facts/hardware/darwin.py:92-132
# lines [92, 93, 94, 95, 98, 99, 100, 101, 102, 103, 105, 106, 110, 113, 115, 116, 117, 118, 121, 123, 124, 125, 126, 127, 128, 130, 132]
# branches ['106->110', '106->132', '115->116', '115->123', '123->124', '123->125', '125->126', '125->127', '127->128', '127->130']

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock(spec=AnsibleModule)
    module_mock.run_command.return_value = (0, 'Pages wired down: 1000\nPages active: 2000\nPages inactive: 3000\n', '')
    return module_mock

@pytest.fixture
def mock_sysctl(mocker):
    return {'hw.memsize': '8589934592'}  # 8 GB

def test_get_memory_facts(mock_module, mock_sysctl, mocker):
    mocker.patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', return_value='/usr/bin/vm_stat')
    darwin_hardware = DarwinHardware(module=mock_module)
    darwin_hardware.sysctl = mock_sysctl

    memory_facts = darwin_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 8192  # 8 GB in MB
    # Pages wired down: 1000 * 4096 bytes
    # Pages active: 2000 * 4096 bytes
    # Pages inactive: 3000 * 4096 bytes
    # Total used: (1000 + 2000 + 3000) * 4096 bytes
    # Total used in MB: (1000 + 2000 + 3000) * 4096 / 1024 / 1024
    total_used_mb = (1000 + 2000 + 3000) * 4096 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 8192 - total_used_mb
