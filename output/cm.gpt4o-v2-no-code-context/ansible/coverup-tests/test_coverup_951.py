# file: lib/ansible/module_utils/facts/hardware/aix.py:218-247
# asked: {"lines": [219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}
# gained: {"lines": [219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module(mocker):
    module = MagicMock()
    module.get_bin_path.side_effect = lambda cmd, required: f"/usr/bin/{cmd}"
    return module

@pytest.fixture
def aix_hardware(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    hardware = AIXHardware(mock_module)
    return hardware

def test_get_device_facts_no_devices(aix_hardware, mocker):
    mocker.patch.object(aix_hardware.module, 'run_command', return_value=(0, "", ""))
    result = aix_hardware.get_device_facts()
    assert result == {'devices': {}}

def test_get_device_facts_with_devices(aix_hardware, mocker):
    lsdev_output = "hdisk0 Available Virtual SCSI Disk Drive\n" \
                   "hdisk1 Defined Virtual SCSI Disk Drive\n"
    lsattr_output_hdisk0 = "size 10G\n" \
                           "location 00-00-00\n"
    lsattr_output_hdisk1 = "size 20G\n" \
                           "location 00-00-01\n"

    def run_command_side_effect(cmd):
        if cmd == "/usr/bin/lsdev":
            return (0, lsdev_output, "")
        elif cmd == ["/usr/bin/lsattr", "-E", "-l", "hdisk0"]:
            return (0, lsattr_output_hdisk0, "")
        elif cmd == ["/usr/bin/lsattr", "-E", "-l", "hdisk1"]:
            return (0, lsattr_output_hdisk1, "")
        return (1, "", "Command not found")

    mocker.patch.object(aix_hardware.module, 'run_command', side_effect=run_command_side_effect)
    
    result = aix_hardware.get_device_facts()
    
    expected_result = {
        'devices': {
            'hdisk0': {
                'state': 'Available',
                'type': 'Virtual SCSI Disk Drive',
                'attributes': {
                    'size': '10G',
                    'location': '00-00-00'
                }
            },
            'hdisk1': {
                'state': 'Defined',
                'type': 'Virtual SCSI Disk Drive',
                'attributes': {
                    'size': '20G',
                    'location': '00-00-01'
                }
            }
        }
    }
    
    assert result == expected_result
