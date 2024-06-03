# file lib/ansible/module_utils/facts/hardware/sunos.py:30-36
# lines [30, 31, 35]
# branches []

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from unittest.mock import Mock

def test_sunos_hardware_initialization():
    # Mock the required 'module' argument
    mock_module = Mock()
    
    # Create an instance of SunOSHardware with the mocked module
    hardware = SunOSHardware(mock_module)
    
    # Assert that the platform attribute is correctly set
    assert hardware.platform == 'SunOS'
    
    # Assert that the instance is indeed a subclass of Hardware
    from ansible.module_utils.facts.hardware.base import Hardware
    assert isinstance(hardware, Hardware)
