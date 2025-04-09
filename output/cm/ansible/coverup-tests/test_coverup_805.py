# file lib/ansible/module_utils/facts/virtual/sunos.py:24-32
# lines [24, 25, 31]
# branches []

import pytest
from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
from unittest.mock import MagicMock

# Since the class SunOSVirtual inherits from a class that requires a 'module' argument,
# we will mock the module argument and pass it to the SunOSVirtual constructor.

def test_sunos_virtual_attributes():
    mock_module = MagicMock()
    sunos_virtual = SunOSVirtual(mock_module)

    assert sunos_virtual.platform == 'SunOS'
    # Add any other attributes to be checked if they are added to the class in the future
