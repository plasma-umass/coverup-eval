# file lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# lines [239, 240, 241]
# branches []

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector

# Assuming the FreeBSDHardware class is defined somewhere in the module
# If not, we would need to mock it or define a dummy class for testing purposes

def test_freebsd_hardware_collector_initialization(mocker):
    # Mock the FreeBSDHardware class to avoid any side effects
    mocker.patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware')

    # Instantiate the FreeBSDHardwareCollector
    collector = FreeBSDHardwareCollector()

    # Assertions to verify postconditions
    assert collector._fact_class is not None
    assert collector._platform == 'FreeBSD'

    # Clean up is handled by the mocker fixture, no side effects should remain
