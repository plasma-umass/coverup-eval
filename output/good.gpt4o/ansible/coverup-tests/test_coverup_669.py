# file lib/ansible/module_utils/facts/hardware/sunos.py:282-286
# lines [282, 283, 284, 286]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the SunOSHardwareCollector and its dependencies are imported correctly
from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector

def test_sunos_hardware_collector():
    with patch('ansible.module_utils.facts.hardware.sunos.HardwareCollector.__init__', return_value=None):
        collector = SunOSHardwareCollector()
        assert collector._fact_class.__name__ == 'SunOSHardware'
        assert collector._platform == 'SunOS'
        assert collector.required_facts == set(['platform'])
