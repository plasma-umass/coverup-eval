# file: lib/ansible/module_utils/facts/collector.py:199-220
# asked: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 206], [216, 217]]}
# gained: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 206], [216, 217]]}

import pytest

# Mock classes to simulate the behavior of collector classes
class MockCollector:
    def __init__(self, name, platform_match_return_value):
        self.name = name
        self._platform_match_return_value = platform_match_return_value

    def platform_match(self, platform):
        return self._platform_match_return_value

def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    # Create mock collector classes
    collector1 = MockCollector('collector1', True)
    collector2 = MockCollector('collector2', False)
    collector3 = MockCollector('collector3', True)

    all_collector_classes = [collector1, collector2, collector3]
    compat_platforms = ['platform1', 'platform2']

    # Call the function with the mock data
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

    # Assertions to verify the correct collectors are found
    assert collector1 in found_collectors
    assert collector2 not in found_collectors
    assert collector3 in found_collectors

# Additional test to cover the case where no collectors match
def test_find_collectors_for_platform_no_match():
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    # Create mock collector classes
    collector1 = MockCollector('collector1', False)
    collector2 = MockCollector('collector2', False)

    all_collector_classes = [collector1, collector2]
    compat_platforms = ['platform1', 'platform2']

    # Call the function with the mock data
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

    # Assertions to verify no collectors are found
    assert len(found_collectors) == 0
