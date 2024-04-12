# file lib/ansible/module_utils/facts/hardware/darwin.py:69-77
# lines [69, 70, 71, 72, 73, 74, 75, 77]
# branches ['72->73', '72->74']

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock(spec=AnsibleModule)
    module_mock.run_command = mocker.MagicMock(return_value=(0, "hw.model: MacBookPro11,4", ""))
    return module_mock

@pytest.fixture
def mock_sysctl(mocker):
    return {
        'kern.osversion': '18G103',
        'kern.osrevision': '199506'
    }

def test_get_mac_facts_success(mock_module, mock_sysctl):
    darwin_hardware = DarwinHardware(module=mock_module)
    darwin_hardware.sysctl = mock_sysctl
    mac_facts = darwin_hardware.get_mac_facts()

    assert mac_facts['model'] == 'MacBookPro11,4'
    assert mac_facts['product_name'] == 'MacBookPro11,4'
    assert mac_facts['osversion'] == '18G103'
    assert mac_facts['osrevision'] == '199506'
    mock_module.run_command.assert_called_once_with("sysctl hw.model")

def test_get_mac_facts_failure(mock_module, mock_sysctl):
    mock_module.run_command.return_value = (1, "", "Error")
    darwin_hardware = DarwinHardware(module=mock_module)
    darwin_hardware.sysctl = mock_sysctl
    mac_facts = darwin_hardware.get_mac_facts()

    assert 'model' not in mac_facts
    assert 'product_name' not in mac_facts
    assert mac_facts['osversion'] == '18G103'
    assert mac_facts['osrevision'] == '199506'
    mock_module.run_command.assert_called_once_with("sysctl hw.model")
