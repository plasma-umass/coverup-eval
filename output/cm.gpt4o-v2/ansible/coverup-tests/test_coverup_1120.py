# file: lib/ansible/module_utils/facts/hardware/aix.py:218-247
# asked: {"lines": [219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}
# gained: {"lines": [219, 220, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247], "branches": [[226, 227], [226, 247], [235, 236], [235, 241]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda cmd, required: f"/usr/bin/{cmd}"
    module.run_command.side_effect = [
        (0, "hdisk0 Available Virtual\nhdisk1 Defined Virtual\n", ""),
        (0, "size 100\nspeed 200\n", ""),
        (0, "size 150\nspeed 250\n", "")
    ]
    return module

@pytest.fixture
def aix_hardware(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hw = AIXHardware(mock_module)
    return aix_hw

def test_get_device_facts(aix_hardware):
    device_facts = aix_hardware.get_device_facts()
    expected_facts = {
        'devices': {
            'hdisk0': {
                'state': 'Available',
                'type': 'Virtual',
                'attributes': {
                    'size': '100',
                    'speed': '200'
                }
            },
            'hdisk1': {
                'state': 'Defined',
                'type': 'Virtual',
                'attributes': {
                    'size': '150',
                    'speed': '250'
                }
            }
        }
    }
    assert device_facts == expected_facts
