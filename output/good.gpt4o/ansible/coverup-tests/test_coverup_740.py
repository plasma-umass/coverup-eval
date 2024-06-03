# file lib/ansible/module_utils/facts/hardware/darwin.py:157-159
# lines [157, 158, 159]
# branches []

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_darwin_hardware_collector():
    # Verify that DarwinHardwareCollector is a subclass of HardwareCollector
    assert issubclass(DarwinHardwareCollector, HardwareCollector)
    
    # Verify that the _fact_class attribute is set correctly
    assert hasattr(DarwinHardwareCollector, '_fact_class')
    assert DarwinHardwareCollector._fact_class.__name__ == 'DarwinHardware'
    
    # Verify that the _platform attribute is set correctly
    assert hasattr(DarwinHardwareCollector, '_platform')
    assert DarwinHardwareCollector._platform == 'Darwin'
