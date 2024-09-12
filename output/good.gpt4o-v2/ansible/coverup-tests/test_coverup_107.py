# file: lib/ansible/module_utils/facts/hardware/freebsd.py:172-189
# asked: {"lines": [172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[179, 180], [179, 189], [181, 182], [181, 189], [183, 184], [183, 185], [186, 181], [186, 187]]}
# gained: {"lines": [172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[179, 180], [179, 189], [181, 182], [181, 189], [183, 184], [186, 181], [186, 187]]}

import os
import pytest
from unittest.mock import patch, Mock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def freebsd_hardware():
    module = Mock()
    return FreeBSDHardware(module)

def test_get_device_facts_with_devices_and_slices(freebsd_hardware):
    mock_dir = ['ada0', 'ada0s1', 'ada1', 'ada1s1', 'da0', 'da0s1', 'acd0']
    expected_result = {
        'devices': {
            'ada0': ['ada0s1'],
            'ada1': ['ada1s1'],
            'da0': ['da0s1'],
            'acd0': []
        }
    }

    with patch('os.path.isdir', return_value=True), \
         patch('os.listdir', return_value=mock_dir):
        result = freebsd_hardware.get_device_facts()
        assert result == expected_result

def test_get_device_facts_with_no_devices(freebsd_hardware):
    mock_dir = []
    expected_result = {'devices': {}}

    with patch('os.path.isdir', return_value=True), \
         patch('os.listdir', return_value=mock_dir):
        result = freebsd_hardware.get_device_facts()
        assert result == expected_result

def test_get_device_facts_with_no_sysdir(freebsd_hardware):
    expected_result = {'devices': {}}

    with patch('os.path.isdir', return_value=False):
        result = freebsd_hardware.get_device_facts()
        assert result == expected_result
