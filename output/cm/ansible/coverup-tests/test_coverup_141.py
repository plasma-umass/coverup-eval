# file lib/ansible/module_utils/facts/hardware/freebsd.py:172-189
# lines [172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189]
# branches ['179->180', '179->189', '181->182', '181->189', '183->184', '183->185', '186->181', '186->187']

import os
import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from unittest.mock import MagicMock

# Define the test function
def test_get_device_facts(mocker):
    # Setup the mock for os.path.isdir and os.listdir
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.listdir', return_value=['ada0', 'ada1', 'ada0s1', 'da0', 'da0s1', 'acd0'])

    # Mock the module parameter required by FreeBSDHardware
    mock_module = MagicMock()

    # Create an instance of the FreeBSDHardware class with the mocked module
    hardware = FreeBSDHardware(module=mock_module)

    # Call the get_device_facts method
    device_facts = hardware.get_device_facts()

    # Assertions to check if the method is working as expected
    assert 'devices' in device_facts
    assert 'ada0' in device_facts['devices']
    assert 'ada1' in device_facts['devices']
    assert 'da0' in device_facts['devices']
    assert 'acd0' in device_facts['devices']
    assert 'ada0s1' in device_facts['devices']['ada0']
    assert 'da0s1' in device_facts['devices']['da0']
    assert len(device_facts['devices']['ada1']) == 0  # ada1 has no slices
    assert len(device_facts['devices']['acd0']) == 0  # acd0 has no slices

# Run the test function
def test_module(mocker):
    test_get_device_facts(mocker)
