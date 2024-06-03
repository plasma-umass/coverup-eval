# file lib/ansible/module_utils/facts/hardware/freebsd.py:172-189
# lines [173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189]
# branches ['179->180', '179->189', '181->182', '181->189', '183->184', '183->185', '186->181', '186->187']

import os
import pytest
import re
from unittest.mock import patch, mock_open, MagicMock

# Assuming the FreeBSDHardware class is imported from the module
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_os_functions(mocker):
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.listdir', return_value=['ada0', 'ada0s1', 'ada1', 'da0', 'da0s1', 'acd0'])

@pytest.fixture
def mock_module():
    return MagicMock()

def test_get_device_facts(mock_os_functions, mock_module):
    hardware = FreeBSDHardware(module=mock_module)
    device_facts = hardware.get_device_facts()

    expected_devices = {
        'ada0': ['ada0s1'],
        'ada1': [],
        'da0': ['da0s1'],
        'acd0': []
    }

    assert 'devices' in device_facts
    assert device_facts['devices'] == expected_devices
