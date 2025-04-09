# file: lib/ansible/module_utils/facts/hardware/aix.py:86-111
# asked: {"lines": [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 102, 103, 104, 105, 106, 107, 108, 109, 111], "branches": [[90, 91], [90, 96], [92, 93], [92, 94], [94, 90], [94, 95], [103, 104], [103, 111]]}
# gained: {"lines": [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 102, 103, 104, 105, 106, 107, 108, 109, 111], "branches": [[90, 91], [90, 96], [92, 93], [92, 94], [94, 90], [94, 95], [103, 104]]}

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    return module

def test_get_memory_facts(mock_module, mocker):
    aix_hardware = AIXHardware(module=mock_module)

    # Mock the run_command method for vmstat -v
    mock_module.run_command = mocker.Mock(return_value=(0, "1000 memory pages\n500 free pages\n", ""))

    # Mock the run_command method for lsps -s
    mock_module.run_command.side_effect = [
        (0, "1000 memory pages\n500 free pages\n", ""),
        (0, "Total Paging Space   Percent Used\n1000MB               20%\n", "")
    ]

    memory_facts = aix_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 1000 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 500 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 1000
    assert memory_facts['swapfree_mb'] == 800
