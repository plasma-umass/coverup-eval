# file lib/ansible/module_utils/facts/hardware/darwin.py:28-41
# lines [28, 29, 40]
# branches []

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.basic import AnsibleModule

def test_darwin_hardware_initialization(mocker):
    # Mock the AnsibleModule to pass as an argument
    mock_module = mocker.Mock(spec=AnsibleModule)

    # Create an instance of DarwinHardware
    hardware = DarwinHardware(module=mock_module)

    # Assertions to verify the initialization
    assert hardware.platform == 'Darwin'
    assert isinstance(hardware, DarwinHardware)
