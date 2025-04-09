# file: lib/ansible/module_utils/facts/hardware/freebsd.py:172-189
# asked: {"lines": [172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[179, 180], [179, 189], [181, 182], [181, 189], [183, 184], [183, 185], [186, 181], [186, 187]]}
# gained: {"lines": [172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[179, 180], [179, 189], [181, 182], [181, 189], [183, 184], [186, 181], [186, 187]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def freebsd_hardware():
    return FreeBSDHardware(None)

def test_get_device_facts_no_devices(freebsd_hardware):
    with patch('os.path.isdir', return_value=True), patch('os.listdir', return_value=[]):
        result = freebsd_hardware.get_device_facts()
        assert result == {'devices': {}}

def test_get_device_facts_with_devices(freebsd_hardware):
    with patch('os.path.isdir', return_value=True), patch('os.listdir', return_value=['ada0', 'ada0s1', 'da0', 'da0s1']):
        result = freebsd_hardware.get_device_facts()
        assert result == {
            'devices': {
                'ada0': ['ada0s1'],
                'da0': ['da0s1']
            }
        }

def test_get_device_facts_no_sysdir(freebsd_hardware):
    with patch('os.path.isdir', return_value=False):
        result = freebsd_hardware.get_device_facts()
        assert result == {'devices': {}}
