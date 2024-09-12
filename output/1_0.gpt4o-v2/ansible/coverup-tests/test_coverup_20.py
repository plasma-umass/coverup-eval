# file: lib/ansible/module_utils/facts/hardware/base.py:35-43
# asked: {"lines": [35, 36, 39, 40, 42, 43], "branches": []}
# gained: {"lines": [35, 36, 39, 40, 42, 43], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.base import Hardware

@pytest.fixture
def mock_module():
    class MockModule:
        pass
    return MockModule()

def test_hardware_init(mock_module):
    hw = Hardware(mock_module, load_on_init=True)
    assert hw.module == mock_module

def test_hardware_populate(mock_module):
    hw = Hardware(mock_module)
    result = hw.populate()
    assert result == {}
