# file lib/ansible/module_utils/facts/virtual/linux.py:27-35
# lines [27, 28, 33]
# branches []

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtual
from unittest.mock import Mock

def test_linux_virtual_class():
    # Mock the required 'module' argument for the Virtual class
    mock_module = Mock()
    
    # Create an instance of the LinuxVirtual class with the mocked module
    linux_virtual = LinuxVirtual(mock_module)
    
    # Assert that the platform attribute is set correctly
    assert linux_virtual.platform == 'Linux'
    
    # Assert that the class docstring is set correctly
    assert LinuxVirtual.__doc__.strip() == (
        "This is a Linux-specific subclass of Virtual.  It defines\n"
        "    - virtualization_type\n"
        "    - virtualization_role"
    )
