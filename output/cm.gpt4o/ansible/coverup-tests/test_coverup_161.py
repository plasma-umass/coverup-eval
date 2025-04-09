# file lib/ansible/module_utils/facts/collector.py:199-220
# lines [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220]
# branches ['204->205', '204->220', '206->204', '206->209', '211->212', '211->214', '216->206', '216->217']

import pytest
from unittest.mock import MagicMock

# Assuming the function is imported from the module
from ansible.module_utils.facts.collector import find_collectors_for_platform

class MockCollector:
    def __init__(self, name, platform_match_return):
        self.name = name
        self._platform_match_return = platform_match_return

    def platform_match(self, platform):
        return self._platform_match_return

def test_find_collectors_for_platform():
    # Mock collector classes
    collector1 = MockCollector(name="collector1", platform_match_return=True)
    collector2 = MockCollector(name="collector2", platform_match_return=False)
    collector3 = MockCollector(name="collector3", platform_match_return=True)
    
    all_collector_classes = [collector1, collector2, collector3]
    compat_platforms = ["platform1", "platform2"]

    # Call the function
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

    # Assertions
    assert collector1 in found_collectors
    assert collector2 not in found_collectors
    assert collector3 in found_collectors
    assert len(found_collectors) == 2

    # Clean up
    del collector1
    del collector2
    del collector3
    del all_collector_classes
    del compat_platforms
    del found_collectors
