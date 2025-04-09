# file lib/ansible/module_utils/facts/virtual/sunos.py:24-32
# lines [24, 25, 31]
# branches []

import pytest
from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
from unittest.mock import Mock

def test_sunos_virtual_class():
    # Mock the required 'module' argument for the Virtual class
    mock_module = Mock()

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Assert that the platform attribute is correctly set
    assert sunos_virtual.platform == 'SunOS'

    # Assert that the instance is of type SunOSVirtual
    assert isinstance(sunos_virtual, SunOSVirtual)

    # Assert that the instance is a subclass of Virtual
    from ansible.module_utils.facts.virtual.base import Virtual
    assert issubclass(SunOSVirtual, Virtual)
