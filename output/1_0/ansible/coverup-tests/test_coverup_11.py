# file lib/ansible/module_utils/facts/hardware/base.py:35-43
# lines [35, 36, 39, 40, 42, 43]
# branches []

import pytest
from ansible.module_utils.facts.hardware.base import Hardware

# Mock module class to pass into Hardware
class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def hardware_instance(mock_module):
    hardware = Hardware(mock_module)
    return hardware

def test_hardware_populate(hardware_instance):
    # Ensure that the populate method returns an empty dictionary
    facts = hardware_instance.populate()
    assert isinstance(facts, dict)
    assert len(facts) == 0

# Clean up is not necessary in this case as the Hardware class does not create any external resources
# that need to be cleaned up after the test. The instances are only in memory and will be garbage collected.
