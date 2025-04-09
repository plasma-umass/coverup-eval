# file: lib/ansible/module_utils/facts/hardware/aix.py:218-247
# asked: {"lines": [218, 219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}
# gained: {"lines": [218, 219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda cmd, required: f"/usr/bin/{cmd}"
    return module

@pytest.fixture
def aix_hardware(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    hardware = AIXHardware(mock_module)
    return hardware

def test_get_device_facts_no_devices(aix_hardware, mock_module):
    mock_module.run_command.return_value = (0, "", "")
    result = aix_hardware.get_device_facts()
    assert result == {'devices': {}}

def test_get_device_facts_single_device(aix_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, "hdisk0 Available Other\n", ""),
        (0, "size 100\nspeed 7200\n", "")
    ]
    result = aix_hardware.get_device_facts()
    assert result == {
        'devices': {
            'hdisk0': {
                'state': 'Available',
                'type': 'Other',
                'attributes': {
                    'size': '100',
                    'speed': '7200'
                }
            }
        }
    }

def test_get_device_facts_multiple_devices(aix_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, "hdisk0 Available Other\nhdisk1 Defined Other\n", ""),
        (0, "size 100\nspeed 7200\n", ""),
        (0, "size 200\nspeed 5400\n", "")
    ]
    result = aix_hardware.get_device_facts()
    assert result == {
        'devices': {
            'hdisk0': {
                'state': 'Available',
                'type': 'Other',
                'attributes': {
                    'size': '100',
                    'speed': '7200'
                }
            },
            'hdisk1': {
                'state': 'Defined',
                'type': 'Other',
                'attributes': {
                    'size': '200',
                    'speed': '5400'
                }
            }
        }
    }
