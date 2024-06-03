# file lib/ansible/module_utils/facts/hardware/aix.py:218-247
# lines [218, 219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247]
# branches ['226->227', '226->247', '235->236', '235->241']

import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.side_effect = lambda cmd, required: f"/usr/bin/{cmd}"
    return module

@pytest.fixture
def aix_hardware(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    return AIXHardware(module=mock_module)

def test_get_device_facts(aix_hardware, mocker):
    mocker.patch.object(aix_hardware.module, 'run_command', side_effect=[
        (0, "hdisk0 Available Other\nhdisk1 Defined Other", ""),
        (0, "size 1000\nspeed 7200", ""),
        (0, "size 2000\nspeed 5400", "")
    ])

    expected_facts = {
        'devices': {
            'hdisk0': {
                'state': 'Available',
                'type': 'Other',
                'attributes': {
                    'size': '1000',
                    'speed': '7200'
                }
            },
            'hdisk1': {
                'state': 'Defined',
                'type': 'Other',
                'attributes': {
                    'size': '2000',
                    'speed': '5400'
                }
            }
        }
    }

    device_facts = aix_hardware.get_device_facts()
    assert device_facts == expected_facts
