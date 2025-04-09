# file lib/ansible/module_utils/facts/hardware/aix.py:218-247
# lines [218, 219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247]
# branches ['226->227', '226->247', '235->236', '235->241']

import pytest
from unittest.mock import MagicMock

# Assuming the AIXHardware class is part of a module named aix
from ansible.module_utils.facts.hardware import aix

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x, y: f"/usr/bin/{x}")
    mock_module.run_command = MagicMock()
    return mock_module

def test_get_device_facts(mock_module, mocker):
    # Mock the run_command method to return predefined lsdev and lsattr outputs
    lsdev_output = "hdisk0 Available Disk Drive\n"
    lsattr_output = "size 100G Disk Size\n"
    mock_module.run_command.side_effect = [
        (0, lsdev_output, ''),
        (0, lsattr_output, '')
    ]

    # Create an instance of the AIXHardware class with the mocked module
    hardware = aix.AIXHardware(module=mock_module)

    # Call the get_device_facts method
    device_facts = hardware.get_device_facts()

    # Assertions to check if the method is returning the expected output
    assert device_facts['devices']['hdisk0']['state'] == 'Available'
    assert device_facts['devices']['hdisk0']['type'] == 'Disk Drive'
    assert device_facts['devices']['hdisk0']['attributes']['size'] == '100G'

    # Verify that the run_command method was called with the expected arguments
    lsdev_cmd = "/usr/bin/lsdev"
    lsattr_cmd = "/usr/bin/lsattr"
    mock_module.run_command.assert_any_call(lsdev_cmd)
    mock_module.run_command.assert_any_call([lsattr_cmd, '-E', '-l', 'hdisk0'])

    # Clean up the mock
    mocker.stopall()
